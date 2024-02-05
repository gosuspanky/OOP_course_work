import json
from abc import ABC, abstractmethod
import requests

from config import DATA_DIR


class AbstractAPI(ABC):

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass


class HeadHunterData(AbstractAPI):

    def __init__(self, user_vacancy):
        self.user_vacancy = user_vacancy
        self.all = []

    def get_data(self):
        self.all.clear()
        params = {
            "text": f'NAME:{self.user_vacancy}',
            "name": "Россия"
        }

        data = requests.get(f'https://api.hh.ru/vacancies', params)

        self.all.extend(json.loads(data.text)['items'])
        return self.all

    def save_data(self):
        data = self.get_data()
        json_data = json.dumps(data, ensure_ascii=False)

        with open(DATA_DIR, 'w', encoding='utf-8') as file:
            file.write(json_data)


if __name__ == '__main__':
    hh_api = HeadHunterData("Python")
    hh_api.save_data()
