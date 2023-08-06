import requests

from API.src.abstract_api import AbstractApi


class SuperJobApi(AbstractApi):

    _id = '2850'
    key = 'v3.r.137727033.a883858aaafb851f3ad9a10955cba220980dd431.8fd4f198788197b0b30ff2dc12aece9ece3619fe'
    base_url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):
        super().__init__()
        self.data = None

    def get_vacancies(self, page=100, keyword='Разработчик, python'):
        # Справочник для параметров GET-запроса
        params = {
            'keyword': keyword,
            'payment_from': 0,
            'count': int(page),     # Количество объявлений на страницу
            'page': 0,              # Страница поиска
        }

        resp = requests.get(self.base_url, headers={"X-Api-App-Id": self.key}, params=params)
        if resp.status_code == 200:
            data = resp.json()
        else:
            raise Exception(f"Ошибка при получении данных: {resp.status_code}")
        return data

    def get_list(self, data):
        pass
