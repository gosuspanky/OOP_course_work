from abc import ABC

from src.hh_data import HeadHunterData, AbstractAPI


def test_issubclass():
    assert issubclass(HeadHunterData, AbstractAPI)
    assert issubclass(AbstractAPI, ABC)


def test_data():
    hh_api = HeadHunterData("Python")
    hh_api.get_data()
    assert len(hh_api.all) > 0
