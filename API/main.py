import json

from API.src.hh import HeadHunterApi


if __name__ == "__main__":

    print("""Данная программа поможет найти нужную вакансию по вашим ключевым словам""")
    keyword = input("Введите ключевые слова для поиска \n")

    hh_api = HeadHunterApi(keyword)
    vacancies = hh_api.get_vacancies()
    formatted_vacancies = hh_api.list_vacancies(vacancies)

    if vacancies:
        with open('data/vacancies.json', 'w', encoding='utf-8') as json_file:
            json.dump(formatted_vacancies, json_file, ensure_ascii=False, indent=4)
    else:
        print("По вашему запросу вакансий не найдено.")


