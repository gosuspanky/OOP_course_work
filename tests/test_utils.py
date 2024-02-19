from src.utils import sort_by_area, get_vacancies_by_salary, get_top_vacancies

area1 = {'area': {'name': 'Казань'}}
area2 = {'area': {'name': 'Москва'}}
area3 = {'area': {'name': 'Казань'}}
area4 = {'area': {'name': 'Питер'}}
area5 = {'area': {'name': 'Казань'}}

unsorted_list = [area1, area2, area3, area4, area5]


def test_sort_by_area():
    assert sort_by_area(unsorted_list, 'Казань') == [area1, area3, area5]


unsorted_list_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
salary_from = 50


def test_get_vacancies_by_salary():
    assert get_vacancies_by_salary(unsorted_list_2, salary_from) == [50, 60, 70, 80, 90]


def test_get_top_vacancies():
    assert get_top_vacancies(unsorted_list_2, 4) == [10, 20, 30, 40]
