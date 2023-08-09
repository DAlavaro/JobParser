# from datetime import datetime
#
#
# def list_vacancies(vacancies__hh):
#     """ Метод для получения стандартизированного списка вакансий"""
#     result = []
#     for vacancy in vacancies__hh:
#         my_dict = {
#             'date': datetime.strptime(vacancy['published_at'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d %B %Y'),
#             'vacancy': vacancy['name'],
#             'company': vacancy['employer']['name'],
#             'salary_low': vacancy["salary"]["from"] if vacancy["salary"] else None,
#             'salary_top': vacancy['salary']['to'] if vacancy["salary"] else None,
#             'employment': vacancy['employment']['name'],
#             'url': vacancy['alternate_url'],
#             'site': 'headhunter',
#         }
#         result.append(my_dict)
#
#
#
#     return result