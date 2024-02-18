from src.vacancy import Vacancy

vacancy = Vacancy('Питона девелопер', 'https://hh.ru', 50_000, 60_000, 'лол',
                  'прикол', 'кек')


def test_init():
    assert vacancy.name == 'Питона девелопер'
    assert vacancy.url == 'https://hh.ru'
    assert vacancy.salary == 50_000
    assert vacancy.description == 'лол'
    assert vacancy.requirements == 'прикол'
    assert vacancy.schedule == 'кек'


user_salary = 50_000
vacancies_list = [Vacancy('Питона девелопер1', 'https://hh.ru', 50_000, 60_000, 'лол',
                          'прикол', 'кек'),
                  Vacancy('Питона девелопер2', 'https://hh.ru', 40_000, 0, 'лол',
                          'прикол', 'кек'),
                  Vacancy('Питона девелопер3', 'https://hh.ru', 0, 70_000, 'лол',
                          'прикол', 'кек'),
                  Vacancy('Питона девелопер4', 'https://hh.ru', 0, 0, 'лол',
                          'прикол', 'кек')
                  ]


def test_ge():
    true_expected_1 = vacancies_list[0] >= vacancies_list[1]
    true_expected_2 = vacancies_list[0] >= user_salary
    false_expected_1 = user_salary >= vacancies_list[2]
    false_expected_2 = vacancies_list[3] >= user_salary

    assert true_expected_1 == True
    assert true_expected_2 == True
    assert false_expected_1 == False
    assert false_expected_2 == False


def test_make_dict():
    vacancy_dict = vacancy.make_dict()
    assert vacancy_dict == {
        'name': 'Питона девелопер',
        'possible_salary': 50_000,
        'description': 'лол',
        'requirements': 'прикол',
        'schedule': 'кек',
        'url': 'https://hh.ru'
    }


def test_str():
    assert vacancy.__str__() == (f'Вакансия: Питона девелопер\n'
                                 f'Возможная З/П: 50000\n'
                                 f'Формат работы: кек\n'
                                 f'Краткое описание: лол\n'
                                 f'Краткие требования: прикол\n'
                                 f'url: https://hh.ru\n\n')


def test_repr():
    assert vacancy.__repr__() == 'Vacancy(Питона девелопер)'


def test_class_method():
    pass
