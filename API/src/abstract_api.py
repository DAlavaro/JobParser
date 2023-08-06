from abc import ABC, abstractmethod



class AbstractApi(ABC):
    base_url = ''

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, page, keyword):
        pass

    @abstractmethod
    def list_vacancies(self, data):
        pass