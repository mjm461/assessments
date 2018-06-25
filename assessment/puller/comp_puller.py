from .county_puller import CountyPuller


class CompPuller(CountyPuller):

    def __init__(self, ncomps=4, labels=None):
        super().__init__()
        if labels is None:
            labels = [('lblSaleDate', 'Sale Date'), ('lblSalePrice', 'Sale Price'),
                      ('lblFinLiv', 'Living Area'), ('lblTotal', 'County Total')]
        self._idheaders = {
            'pnlComps': ('Comp', self.extract_comps)
        }
        self._labels = labels
        self._ncomps = ncomps

    @property
    def page(self):
        return "Comps"

    @property
    def headers(self):
        return [h[0] + " " + l[-1] + " " + str(i)
                for l in self._labels
                for i in range(1, self._ncomps + 1)
                for h in self.idheaders.values()]

    @property
    def idheaders(self):
        return self._idheaders

    def extract_comps(self, parcel_id, header, html):
        comps = []

        comp_divs = html.find('div', id=parcel_id)
        if comp_divs:
            for i in range(1, self._ncomps + 1):
                for label, column in self._labels:
                    comp = html.find('span', id="".join([label, str(i)]))
                    comps.append((" " .join([header, column, str(i)]), self.substitute(comp.text) if comp else ""))

        return comps
