from src.hh_data import HeadHunterData
from src.vacancy import Vacancy


def get_vacancies_by_salary(vacancies_list, salary_from):
    ranged_vacancies = []

    for vac_dict in vacancies_list:
        vacancy = Vacancy(vac_dict['name'])

        vacancy.url = vac_dict['url']
        vacancy.description = vac_dict['description']
        vacancy.requirements = vac_dict['requirements']
        vacancy.schedule = vac_dict['schedule']
        vacancy.employment = vac_dict['employment']

        if vac_dict['salary_from'] > 0:
            vacancy.salary = vac_dict['salary_from']
        elif vac_dict['salary_from'] == 0 and vac_dict['salary_to'] > 0:
            vacancy.salary = vac_dict['salary_to']
        else:
            vacancy.salary = 0

        if vacancy >= salary_from:
            ranged_vacancies.append(vacancy)

    return ranged_vacancies


def get_top_vacancies(ranged_vacancies, num):
    return ranged_vacancies[:num]


def print_vacancies(top_vacancies):
    for i in range(len(top_vacancies)):
        print(top_vacancies[i])


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    hh_api = HeadHunterData(search_query)
    hh_api.save_vacancies()

    user_area = input('Введите город в котором ищите вакансию\n').title()
    hh_vacancies = hh_api.sort_by_area(user_area)
    hh_api.save_sorted_vacancies()

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(vacancies_list)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    salary_from = int(input("Укажите зарплату, от какой суммы веси поиск:\n"))

    ranged_vacancies = get_vacancies_by_salary(vacancies_list, salary_from)

    ranged_vacancies.sort(key=lambda vacancy: vacancy.salary, reverse=True)

    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

    print_vacancies(top_vacancies)


if __name__ == '__main__':
    user_interaction()
