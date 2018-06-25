from .county_puller import CountyPuller


class BuildingPuller(CountyPuller):

    def __init__(self):
        super().__init__()
        self._idheaders = {
            'lblResTotRooms': 'Total Rooms',
            'lblResBasement': 'Basement',
            'lblResBedrooms': 'Bedroom',
            'lblGrade': 'Grade',
            'lblResFullBath': 'Full Bath',
            'lblResHalfBath': 'Half Bath',
            'lblResLiveArea': 'Living Area',
            'lblResGarage': 'Garage',
            'lblFireplace': 'Fire Place',
            'lblResYearBuilt': 'Year Built',
        }

    @property
    def page(self):
        return "Building"

    @property
    def headers(self):
        return self.idheaders.values()

    @property
    def idheaders(self):
        return self._idheaders
