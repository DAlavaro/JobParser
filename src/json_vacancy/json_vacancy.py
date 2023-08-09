import json
from datetime import datetime

from src.json_vacancy.abstract_json_vacancy import AbstractJsonVacancy


class JsonVacancy(AbstractJsonVacancy):
    def __init__(self, path, data):
        self.path = path
        self.data = data

    def get_vacancy(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def len_vacancy(self):
        return len(self.data)

    # def print_vacancy(self):
    #     with open(VACANCIES, 'r', encoding='utf-8') as file:
    #         files = json.load(file)
    #         for file in files:
    #             print(f"Дата публикации объявления {file['date']}")

    def add_vacancies(self):
        pass

    def filter_vacancies(self, key_filter):
        result = []
        for i in self.data:
            if i['salary_top'] == None:
                if i['salary_low'] == None:
                    i['salary_top'] = 0
                else:
                    i['salary_top'] = i['salary_low']
            if i['salary_top'] >= int(key_filter):
                result.append(i)
        self.data = result

    def sorted_vacancies(self, key=0):
        if key == '1':
            self.data = sorted(self.data, key=lambda x: datetime.strptime(x['date'], '%d %B %Y'), reverse=True)
        elif key == '2':
            self.data = sorted(self.data, key=lambda x: int(x['salary_top']))
        elif key == '3':
            self.data = sorted(self.data, key=lambda x: int(x['salary_top']), reverse=True)
        self.data = sorted(self.data, key=lambda x: datetime.strptime(x['date'], '%d %B %Y'))

    def delete_vacancies(self):
        pass
