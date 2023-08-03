from API.abstract_api import AbstractApi
import requests

class HeadHanterApi(AbstractApi):
    base_url = 'https://api.hh.ru/vacancies'

    def __init__(self):
        super().__init__()

    def get_vacancies(self, page=0):
        # Справочник для параметров GET-запроса
        params = {
            'text': 'Python',
            'name': 'Разработчик',
            'area': 1,
            'page': page,
            'per_page': 100,
        }

        response = requests.get(self.base_url, params)
        if response.status_code == 200:
            data = response.content.decode()
        else:
            raise Exception(f"Ошибка при получении данных: {response.status_code}")
        response.close()
        return data
