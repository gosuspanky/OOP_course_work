from config import TXT_OUTPUT_DIR, JSON_OUTPUT_DIR
from src.hh_data import HeadHunterData
from src.save_vacancies import TXTSaver, JSONSaver
from src.utils import sort_by_area, get_vacancies_by_salary, get_top_vacancies, make_dict_from_vacancy
from src.vacancy import Vacancy


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

        # преобразуем список экземпляров класса в список словарей
        vacancies_dict_list = make_dict_from_vacancy(top_vacancies)

        save_to_txt = TXTSaver(TXT_OUTPUT_DIR)
        save_to_json = JSONSaver(JSON_OUTPUT_DIR)
        save_to_json.write_data(vacancies_dict_list)

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
    user_interaction()
