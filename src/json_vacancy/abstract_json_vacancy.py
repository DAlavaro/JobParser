from abc import ABC, abstractmethod


class AbstractJsonVacancy(ABC):

    @abstractmethod
    def get_vacancy(self, API_list):
        pass

    def print_vacancy(self):
        pass

    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def filter_vacancies(self):
        pass

    @abstractmethod
    def sorted_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass






