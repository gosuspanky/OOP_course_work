import json

from config import DATA_DIR


class Vacancy:

    def __init__(self, name):
        self.name = name

        self.url = None
        self.salary = None
        self.description = None
        self.requirements = None
        self.schedule = None
        self.employment = None

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        else:
            return self.salary > other

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        else:
            return self.salary >= other

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        else:
            return self.salary < other

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        else:
            return self.salary <= other

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        else:
            return self.salary == other

    def check_data(self):
        pass

    def __repr__(self):
        return f'Vacancy({self.name})'

    def __str__(self):
        return (f'Вакансия: {self.name}\n'
                f'Примерная предлагаемая З/П: {self.salary}\n'
                f'Ссылка на вакансию: {self.url}\n'
                f'Краткое описание вакансии: {self.description}\n'
                f'Краткие требования вакансии: {self.requirements}\n'
                f'Формат работы: {self.schedule}\n')

    @staticmethod
    def cast_to_object_list(sorted_list):
        reworked_dicts = []

        for i in range(len(sorted_list)):
            name = sorted_list[i]['name']
            url = sorted_list[i]['alternate_url']

            if sorted_list[i]['salary'] is not None:
                if sorted_list[i]['salary']['from'] is not None:

                    salary_from = sorted_list[i]['salary']['from']
                else:
                    salary_from = 0

                if sorted_list[i]['salary']['to'] is not None:
                    salary_to = sorted_list[i]['salary']['to']
                else:
                    salary_to = 0
            else:

                salary_from, salary_to = 0, 0

            description = sorted_list[i]['snippet']['responsibility']
            requirements = sorted_list[i]['snippet']['requirement']
            schedule = sorted_list[i]['schedule']['name']
            employment = sorted_list[i]['employment']['name']

            vacancy_dict = {
                'name': name,
                'url': url,
                'salary_from': salary_from,
                'salary_to': salary_to,
                'description': description,
                'requirements': requirements,
                'schedule': schedule,
                'employment': employment
            }

            reworked_dicts.append(vacancy_dict)

        return reworked_dicts


if __name__ == '__main__':
    pass
