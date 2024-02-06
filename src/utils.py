from src.hh_data import HeadHunterData
from src.vacancy import Vacancy


def filter_vacancies(vacancies_list, filter_words):
    pass


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    pass


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    hh_api = HeadHunterData(search_query)
    hh_api.save_vacancies()

    user_area = input('Введите город в котором ищите вакансию\n').title()
    hh_vacancies = hh_api.sort_by_area(user_area)
    hh_api.save_sorted_vacancies()

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    filter_words = input("Введите ключевые слова для фильтрации вакансий (без запятых через пробел):\n"
                         'Например: "Стажировка", "Полная занятость", "Стажер-программист", "Разбработчик"\n').split()

    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
