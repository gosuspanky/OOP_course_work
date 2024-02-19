from src.hh_data import HeadHunterData
from src.save_vacancies import JSONSaver, TXTSaver
from src.vacancy import Vacancy
from config import JSON_OUTPUT_DIR, TXT_OUTPUT_DIR


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


# Функция для взаимодействия с пользователем
def user_interaction():
    """
    Функция взаимодействия с пользователем
    """
    while True:
        search_query = input("Введите поисковый запрос: ")
        print('Веду поиск, собираю данные...')
        hh_api = HeadHunterData(search_query)
        vacancies = hh_api.get_vacancies()

        user_area = input('Введите город в котором ищите вакансию\n'
                          '(на русском языке название города)\n'
                          '(Если введете город не верно, то список вакансий будет пустым)\n').title()

        user_area_vacancies = sort_by_area(vacancies, user_area)  # сортируем по городу

        vacancies_list = Vacancy.cast_to_object_list(user_area_vacancies)  # создаем список экземпляров класса

        try:
            user_salary = int(input("Укажите зарплату, от какой суммы вести поиск:\n"))
            top_n = int(input("Введите количество вакансий для вывода в топ N:\n"))
        except ValueError:
            raise ValueError('Ошибка значения! Введенное значение не является числом, перезапустите программу!')

        ranged_vacancies = get_vacancies_by_salary(vacancies_list, user_salary)  # фильтруем по желаемой зп

        sorted_vacancies = sorted(ranged_vacancies, reverse=True)  # сортируем полученный список

        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)  # отсекаем лишнее для вывода топа

        vacancies_list = []
        for i in range(len(top_vacancies)):
            vacancy = top_vacancies[i]
            vacancy_dict = vacancy.make_dict()
            vacancies_list.append(vacancy_dict)

        save_to_txt = TXTSaver(TXT_OUTPUT_DIR)
        save_to_json = JSONSaver(JSON_OUTPUT_DIR)
        save_to_json.write_data(vacancies_list)

        user_input = input('Сохранить отсортированные вакансии в файле TXT? (д/н): ')
        if user_input == 'д':
            save_to_txt.write_data(top_vacancies)
        elif user_input == 'н':
            continue
        else:
            raise ValueError('Введено неверное значение, перезапустите программу')

        user_input = input('Продолжить работу с программой? (д/н): ').lower()
        if user_input == 'д':
            user_input = input('Отчистить прошлые данные? (д/н): ').lower()
            if user_input == 'д':
                save_to_json.delete_data()
                save_to_txt.delete_data()
            elif user_input == 'н':
                continue
            else:
                raise ValueError('Введено неверное значение, перезапустите программу')
            continue
        elif user_input == 'н':
            break
        else:
            raise ValueError('Введено неверное значение, перезапустите программу')


if __name__ == '__main__':
    pass