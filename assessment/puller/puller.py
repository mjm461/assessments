import abc


class Puller(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def headers(self):
        pass

    @abc.abstractmethod
    def parse(self, parsel_id):
        pass
