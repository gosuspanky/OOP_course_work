import json
from abc import ABC, abstractmethod

from config import JSON_OUTPUT_DIR
from src.vacancy import Vacancy


class SaveData(ABC):

    @abstractmethod
    def write_data(self, data):
        pass


class JSONSaver(SaveData):

    def __init__(self, file_path):
        self.file_path = file_path

    def delete_data(self):
        empty_list = []
        with open(self.file_path, 'w') as file:
            json.dump(empty_list, file)

    def write_data(self, data):
        with open(self.file_path, 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)


class TXTSaver(SaveData):

    def __init__(self, file_path):
        self.file_path = file_path

    def delete_data(self):
        empty_str = ''
        with open(self.file_path, 'w') as file:
            file.write(empty_str)

    def write_data(self, data):
        with open(self.file_path, 'a', encoding='utf-8') as file:
            for i in range(len(data)):
                file.write(data[i])


if __name__ == '__main__':
    # vacancy_dict = {
    #     'name': 'Питона разраб',
    #     'possible_salary': 80_000,
    #     'description': "self.description",
    #     'requirements': "self.requirements",
    #     'schedule': "self.schedule",
    #     'url': "self.url"
    # }
    # saver = JSONSaver(JSON_OUTPUT_DIR)
    # saver.write_data([vacancy_dict])
    pass
