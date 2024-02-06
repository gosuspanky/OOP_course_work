import json

from config import DATA_DIR


class Vacancy:

    def __init__(self):
        self.name = None
        self.url = None
        self.salary = None
        self.description = None
        self.requirements = None

    def salary_compare(self):
        pass

    def check_data(self):
        pass

    @staticmethod
    def cast_to_object_list(sorted_list):
        reworked_dicts = []

        for i in range(len(sorted_list)):
            name = sorted_list[i]['name']
            url = sorted_list[i]['alternate_url']
            salary = sorted_list[i]['salary']
            description = sorted_list[i]['snippet']['responsibility']
            requirements = sorted_list[i]['snippet']['requirement']
            schedule = sorted_list[i]['schedule']['name']
            employment = sorted_list[i]['employment']['name']

            vacancy_dict = {
                'name': name,
                'url': url,
                'salary': salary,
                'description': description,
                'requirements': requirements,
                'schedule': schedule,
                'employment': employment
            }

            reworked_dicts.append(vacancy_dict)

        return reworked_dicts


if __name__ == '__main__':
    pass
