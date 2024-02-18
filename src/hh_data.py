import json
from abc import ABC, abstractmethod
import requests
import time


class AbstractAPI(ABC):
    """
    Абстрактный метод для класса получения данных по API
    """

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterData(AbstractAPI):
    """
    Класс получения данных по API
    """

    def __init__(self, search_req):
        self.search_req = search_req

        self.all_list = []
        self.sorted_list = []

    def get_vacancies(self):
        """
        Метод получения данных по определенным параметрам с сайта HH
        :return:
        """
        for page in range(0, 10):

            params = {
                "text": f'NAME:{self.search_req}',
                "area": 113,
                'page': page,
                'per_page': 100,
                "only_with_salary": True
            }

            req = requests.get(f'https://api.hh.ru/vacancies', params)
            json_obj = req.content.decode()

            data = json.loads(json_obj)

            if (data['pages'] - page) <= 1:
                break

            time.sleep(0.25)

            self.all_list.extend(data['items'])

        return self.all_list


if __name__ == '__main__':
    pass

