from . import Puller, AppealPuller, BuildingPuller, CompPuller, GeneralInfoPuller, ZillowPuller

from functools import reduce


class AggregatePuller(Puller):

    def __init__(self, zwid=None):
        super().__init__()
        self._pullers = [p() for p in [AppealPuller, BuildingPuller, CompPuller, GeneralInfoPuller]]
        self._zillow_puller = None
        if zwid:
            self._zillow_puller = ZillowPuller(zwid)

    @property
    def headers(self):
        return [h for p in self._pullers + ([self._zillow_puller] if self._zillow_puller else []) for h in p.headers]

    def parse(self, id):
        assessment = reduce(lambda a, b: dict(a, **b), [p.parse(id) for p in self._pullers])
        if self._zillow_puller and 'Address' in assessment:
            assessment = {**assessment, **self._zillow_puller.parse(assessment['Address'])}
        return assessment
