import json
from abc import ABC, abstractmethod
import requests

from config import DATA_DIR, SORTED_DATA_DIR


class AbstractAPI(ABC):

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass


class HeadHunterData(AbstractAPI):

    def __init__(self, vacancy):
        self.vacancy = vacancy

        self.all = []
        self.sorted_list = []

    def get_data(self):
        self.all.clear()
        params = {
            "text": f'NAME:{self.vacancy}',
            "area": 113,
            'per_page': 100
        }

        data = requests.get(f'https://api.hh.ru/vacancies', params)

        self.all.extend(json.loads(data.text)['items'])

        return self.all

    def sort_by_area(self, area: str):
        self.sorted_list.clear()

        for i in range(len(self.all)):
            if self.all[i]['area']['name'] == area:
                self.sorted_list.append(self.all[i])
        return self.sorted_list

    def save_data(self):
        data = self.get_data()
        json_data = json.dumps(data, ensure_ascii=False)

        with open(DATA_DIR, 'w', encoding='utf-8') as file:
            file.write(json_data)

    def save_sorted_data(self):

        json_data = json.dumps(self.sorted_list, ensure_ascii=False)
        with open(SORTED_DATA_DIR, 'w', encoding='utf-8') as file:
            file.write(json_data)


if __name__ == '__main__':
    user_vacancy = input('Введите название вакансии или ключевое слово для поиска вакансий\n')
    hh_api = HeadHunterData(user_vacancy)
    hh_api.save_data()

    user_area = input('Введите город в котором ищите вакансию\n').title()
    hh_api.sort_by_area(user_area)
    hh_api.save_sorted_data()
    print(hh_api.sorted_list)