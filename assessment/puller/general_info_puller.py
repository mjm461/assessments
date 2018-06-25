from .county_puller import CountyPuller


class GeneralInfoPuller(CountyPuller):
    def __init__(self):
        super().__init__()
        self._idheaders = {
            'BasicInfo1_lblAddress': 'Address',
            'lblCountyTot': 'County Total',
            'BasicInfo1_lblParcelID': 'Parcel Id',
            'lblSalePrice': 'Sale Price',
            'lblSaleDate': 'Sale Date',
            'lblCountyLand': 'County Land Value',
            'lblCountyBuild': 'County Building Value',
            'lblLot': 'Lot Area'
        }

    @property
    def page(self):
        return "GeneralInfo"

    @property
    def headers(self):
        return self.idheaders.values()

    @property
    def idheaders(self):
        return self._idheaders
