from settings import VACANCIES
from src.API.headhunter import HeadHunterApi
from src.API.super_job import SuperJobApi
from src.json_vacancy.json_vacancy import JsonVacancy


def main_func():
    # Очищаем файл с вакансиями
    f = open(VACANCIES, 'w+')
    f.close()

    print("""Данная программа поможет найти нужную вакансию по вашим ключевым словам""")
    keyword = input("Введите ключевые слова для поиска подходящей вакансии\n")

    # Создаем список вакансий hh
    hh_api = HeadHunterApi(keyword)
    vacancies_hh = hh_api.get_vacancies()
    list_hh = hh_api.list_vacancies(vacancies_hh)

    # Создаем список вакансий sj
    sj_api = SuperJobApi(keyword)
    vacancies_sj = sj_api.get_vacancies()
    list_sj = sj_api.list_vacancies(vacancies_sj)

    # Создаем экземпляр класса для записи вакансий в файл
    data = list_sj + list_hh
    json_vacancy = JsonVacancy(VACANCIES, data)

    # Записываем данные о полученных вакансиях в файл
    if vacancies_sj:
        json_vacancy.get_vacancy()
        print(f"Отлично по вашему запросу найдено {json_vacancy.len_vacancy()} вакансий")
    else:
        print("По вашему запросу вакансий не найдено.")

    # Фильтруем полученные данные по заработной плате
    key_filer = input("Сократите количество запросов указав минимальный размер желаемой заработной платы\n")
    json_vacancy.filter_vacancies(key_filer)
    print(f"Отлично по вашему запросу найдено {json_vacancy.len_vacancy()} вакансий")

    print("По умолчанию вакансии отсортированы по дате от самой свежей")
    key_sorted = input("""Вы можете выбрать сортировку 
        1 - Обратная сортировка по дате 
        2 - Сортировка по зарплате от максимального значения к минимальному
        3 - Сортировка по зарплате от минимального значения к  максимальному
        любой другой символ - Оставит сортировку без изменений\n""")
    json_vacancy.sorted_vacancies(key_sorted)
    print("Вакансии отсортированы в соответствии с вашим запросом")
    json_vacancy.print_vacancy()