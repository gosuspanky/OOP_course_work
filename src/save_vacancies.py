import json
from abc import ABC, abstractmethod


class SaveData(ABC):
    """
    Абстрактный класс для сохранения данных в файл
    """

    @abstractmethod
    def write_data(self, data):
        pass


class JSONSaver(SaveData):
    """
    Класс, сохраняющий данные в .json формате
    на вход получаем путь до файла и данные для записи
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def delete_data(self):
        empty_list = []
        with open(self.file_path, 'w') as file:
            json.dump(empty_list, file)

    def write_data(self, data):
        json_data = json.dumps(data, ensure_ascii=False)

        with open(self.file_path, 'a', encoding='windows-1251') as file:
            file.write(json_data)


class TXTSaver(SaveData):
    """
    Класс, который сохраняет описание вакансий в .txt формате
    на вход получаем путь до файла и данные для записи
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def delete_data(self):
        empty_str = ''
        with open(self.file_path, 'w') as file:
            file.write(empty_str)

    def write_data(self, data):
        with open(self.file_path, 'a', encoding='windows-1251') as file:
            for i in range(len(data)):
                vacancy = data[i]
                file.write(vacancy.__str__())
