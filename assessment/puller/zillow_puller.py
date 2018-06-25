from .puller import Puller
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
import re


class ZillowPuller(Puller):
    def __init__(self, zwid):
        super().__init__()
        self._headers = ['Zillow Estimate', 'Zillow Last Sold']
        self._zillow_data = ZillowWrapper(zwid)

    @property
    def headers(self):
        return self._headers

    def parse(self, address):
        address, zip_code, _  = re.search(r'(.*)(\d{5}(-\d{4})?)$', address).groups()
        result = GetDeepSearchResults(self._zillow_data.get_deep_search_results(address, zip_code))
        return {
            self.headers[0]: result.zestimate_amount,
            self.headers[1]: result.last_sold_date
        }
