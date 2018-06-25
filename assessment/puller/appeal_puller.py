from .county_puller import CountyPuller


class AppealPuller(CountyPuller):

    def __init__(self):
        super().__init__()
        self._idheaders = {
            'dgAppealInfo': ('Appeal Status', self.extract_appeal)
        }

    @property
    def page(self):
        return "Appeal"

    @property
    def headers(self):
        return [ v[0] for v in self.idheaders.values()]

    @property
    def idheaders(self):
        return self._idheaders

    def extract_appeal(self, parcel_id, header, html):
        appeal = ""

        appeal_table = html.find('table', id=parcel_id)
        if appeal_table:
            # join all tr and td in table with a space
            appeal = " ".join([(str(c.text)) for r in appeal_table.findAll('tr') for c in r.findAll('td')])

        return [(header, self.substitute(appeal))]
