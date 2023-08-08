import json

from settings import HH_VACANCIES
from src.json_vacancy.abstract_json_vacancy import AbstractJsonVacancy


class JsonVacancy(AbstractJsonVacancy):
    def __init__(self, path=HH_VACANCIES):
        self.path = path

    def get_vacancy(self, API_list):
        with open(HH_VACANCIES, 'w', encoding='utf-8') as file:
            json.dump(API_list, file, ensure_ascii=False, indent=4)

    def print_vacancy(self):
        with open(HH_VACANCIES, 'r', encoding='utf-8') as file:
            files = json.load(file)
            for file in files:
                print(f"Дата публикации объявления {file['date']}")

            return file

    def add_vacancies(self):
        pass

    def filter_vacancies(self):
        pass

    def sorted_vacancies(self):
        pass

    def delete_vacancies(self):
        pass


