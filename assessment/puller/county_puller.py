from .puller import Puller

import re
import abc
import os
import requests
from bs4 import BeautifulSoup


class CountyPuller(Puller, metaclass=abc.ABCMeta):
    _substitutions = [
        (r',', ''),
        (r'\$', ' '),
        (r'[Ss][Qq][Ff][Tt]', ''),
        (r'<.+?>', ' '),
        (r'\s+', ' ')
    ]

    def __init__(self, cache_dir='data'):

        self._base_url = 'http://www2.county.allegheny.pa.us/RealEstate/%s.aspx?ParcelID=%s'

        self._cache_dir = cache_dir

    @abc.abstractmethod
    def page(self):
        pass

    @abc.abstractmethod
    def idheaders(self):
        pass

    @property
    def substitutions(self):
        return self._substitutions

    def _url(self, parcel_id):
        return self._base_url % (self.page, parcel_id)

    def _extract(self, parcel_id, header, html):
        text = html.find(id=parcel_id)
        if text:
            text = text.text
        else:
            text = ""
        return [(header, self.substitute(text))]

    def _parse(self, parsed_html):
        items = []
        for html_id, header in self.idheaders.items():
            if isinstance(header, tuple):
                header, extract = header
            else:
                extract = self._extract

            items.append(extract(html_id, header, parsed_html))

        return dict(inner for outer in items for inner in outer)

    def substitute(self, text):
        if self.substitutions:
            for target, replace in self.substitutions:
                text = re.sub(target, replace, text, flags=re.UNICODE)
        return text

    def parse(self, parsel_id):
        try:
            data = os.path.join(self._cache_dir, parsel_id + "-" + self.page + ".html")
        except:
            print(parsel_id)
        if not os.path.exists(data):
            html = requests.get(self._url(parsel_id)).text
            with open(data, 'w') as fout:
                fout.write(html)
        else:
            html = open(data, 'r').read()

        parsed_html = BeautifulSoup(html, 'html.parser')

        for br in parsed_html.find_all("br"):
            br.replace_with("\n")

        return self._parse(parsed_html)
