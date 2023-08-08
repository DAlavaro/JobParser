from settings import HH_VACANCIES
from src.API.hh import HeadHunterApi
from src.json_vacancy.json_vacancy import JsonVacancy
from utils.utils import list_vacancies

if __name__ == "__main__":
    # Очищаем файл с вакансиями
    f = open(HH_VACANCIES, 'w+')
    f.close()

    print("""Данная программа поможет найти нужную вакансию по вашим ключевым словам""")
    keyword = input("Введите ключевые слова для поиска \n")

    hh_api = HeadHunterApi(keyword)
    vacancies = hh_api.get_vacancies()
    API_list = list_vacancies(vacancies)
    JVacansy = JsonVacancy()

    # Записываем данные о полученных вакансиях в файл
    if vacancies:
        json_info = JVacansy.get_vacancy(API_list)
    else:
        print("По вашему запросу вакансий не найдено.")

    JVacansy.print_vacancy()
