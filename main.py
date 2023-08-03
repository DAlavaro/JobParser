from API.hh import HeadHanterApi

if __name__ == "__main__":

    hh_api = HeadHanterApi()



    print("Vacancies from HeadHunter:")
    vacancies_hh = hh_api.get_vacancies()
    print(vacancies_hh)