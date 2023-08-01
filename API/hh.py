# библитека для работы с HTTP-запросами
import requests
import json
import time

def get_page(page=0):
    """
    Создаем метод для получения страницы со списком вакансий.
    Аргументы:
        page - Индекс страницы начиная с 0. Значение по умолчанию 0 т.е. первая страница
    """

    # Справочник для параметров GET-запроса
    params = {
        'text': 'NAME: Аналитик',
        'area': 1,
        'page': page,
        'per_page': 100
    }

    req = requests.get('https://api.hh.ru/vacancies', params)   # Посылаем запрос к API
    data = req.content.decode()                                 # Декодирует ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data

# Создадим список, в котором будут храниться ответы к сервису API hh.ru
js_objs = []

# Считываем первые 2000 вакансий
for page in range(0, 20):

    # преобразуем текст ответа запроса в словарь Python
    js_obj = json.loads(get_page(page))

    # Добавим текущий ответ запроса в список
    js_objs.extend(js_obj["items"])

    # Проверка на последнюю страницу, если вакансий меньше 2000
    if (js_obj["pages"] - page) <= 1:
        break

    # Не обязательная задержка, но чтобы не нагружать сервисы hh, оставим 5 сек
    time.sleep(0.25)

print("Страницы поиска собраны")
print(js_objs)