import json
from abc import ABC, abstractmethod
import requests
import time

from config import DATA_DIR, SORTED_DATA_DIR


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterData(AbstractAPI):

    def __init__(self, search_req):
        self.search_req = search_req

        self.all_list = []
        self.sorted_list = []

    def get_vacancies(self):
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

    # def save_vacancies(self):
    #     data = self.get_vacancies()
    #     json_data = json.dumps(data, ensure_ascii=False)
    #
    #     with open(DATA_DIR, 'w', encoding='utf-8') as file:
    #         file.write(json_data)

    # def save_sorted_vacancies(self):
    #
    #     json_data = json.dumps(self.sorted_list, ensure_ascii=False)
    #     with open(SORTED_DATA_DIR, 'w', encoding='utf-8') as file:
    #         file.write(json_data)

    # def sort_by_area(self, area: str):
    #     self.sorted_list.clear()
    #
    #     for i in range(len(self.all)):
    #         if self.all[i]['area']['name'] == area:
    #             self.sorted_list.append(self.all[i])
    #     return self.sorted_list


if __name__ == '__main__':
    # user_vacancy = input('Введите название вакансии или ключевое слово для поиска вакансий\n')
    hh_api = HeadHunterData('Python')
    hh_api.get_vacancies()

    # user_area = input('Введите город в котором ищите вакансию\n').title()
    # hh_api.sort_by_area(user_area)
    # hh_api.save_sorted_data()
    # hh_api.filter_for_vacancies()
    #
    # print(hh_api.reworked_dicts)
