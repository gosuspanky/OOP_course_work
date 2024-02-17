import json

from config import DATA_DIR


class Vacancy:

    def __init__(self, name, url, salary_from, salary_to, description, requirements, schedule):
        self.name = name

        self.url = url
        self.description = description
        self.requirements = requirements
        self.schedule = schedule

        if salary_from > 0:
            self.salary = salary_from
        elif salary_from == 0 and salary_to > 0:
            self.salary = salary_to
        else:
            self.salary = 0

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

    def make_dict(self):

        vacancy_dict = {
            'name': self.name,
            'possible_salary': self.salary,
            'description': self.description,
            'requirements': self.requirements,
            'schedule': self.schedule,
            'url': self.url
        }

        return vacancy_dict

    def __repr__(self):
        return f'{__class__.__name__}({self.name})'

    def __str__(self):
        return (f'vacancy_name: {self.name}\n'
                f'possible_salary: {self.salary}\n'
                f'work_format: {self.schedule}\n'
                f'short_description: {self.description}\n'
                f'short_requirements: {self.requirements}\n'
                f'url: {self.url}\n')

    @classmethod
    def cast_to_object_list(cls, sorted_list):
        vacancies_list = []

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

            vacancy = cls(name, url, salary_from, salary_to, description, requirements, schedule)

            vacancies_list.append(vacancy)

        return vacancies_list


if __name__ == '__main__':
    pass
