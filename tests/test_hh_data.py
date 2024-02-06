from abc import ABC

from src.hh_data import HeadHunterData, AbstractAPI


def test_issubclass():
    assert issubclass(HeadHunterData, AbstractAPI)
    assert issubclass(AbstractAPI, ABC)


def test_data():
    hh_api = HeadHunterData("Python")
    hh_api.get_vacancies()
    assert len(hh_api.all) > 0


def test_sorted_data():
    v = HeadHunterData("Python")
    v.get_vacancies()
    v.sort_by_area('Казань')

    assert len(v.sorted_list) > 0
