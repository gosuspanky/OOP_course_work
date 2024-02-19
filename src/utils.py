def sort_by_area(vacancies, area: str):
    """
    Функция для фильтрации полученных данных с сайта по городу

    :param vacancies: список словарей, полученных с сайта HH
    :param area: вводимый пользователем город
    :return: отсортированный список словарей по городу
    """
    sorted_list = []

    for i in range(len(vacancies)):
        if vacancies[i]['area']['name'] == area:
            sorted_list.append(vacancies[i])
    return sorted_list


def get_vacancies_by_salary(vacancies_list, salary_from):
    """
    Функция сортировки по уровню желаемой З/П
    :param vacancies_list: список экземпляров класса Vacancy
    :param salary_from: сумма З/П вводимого пользователем
    :return: отсортированный список
    """
    ranged_vacancies = []

    for vacancy in vacancies_list:

        if vacancy >= salary_from:
            ranged_vacancies.append(vacancy)

    return ranged_vacancies


def get_top_vacancies(ranged_vacancies, num):
    """
    Функция для отсечения вакансий
    :param ranged_vacancies: список вакансий
    :param num: количество вакансий для вывода
    :return: нужное количество вакансий
    """
    return ranged_vacancies[:num]


def print_vacancies(top_vacancies):
    """
    Функция вывода описания вакансий
    :param top_vacancies: список вакансий
    """
    for i in range(len(top_vacancies)):
        print(top_vacancies[i])


def make_dict_from_vacancy(data):
    vacancies_list = []
    for i in range(len(data)):
        vacancy = data[i]
        vacancy_dict = vacancy.make_dict()
        vacancies_list.append(vacancy_dict)

    return vacancies_list
