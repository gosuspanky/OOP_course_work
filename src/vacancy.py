class Vacancy:
    """
    Класс Вакансии
    """

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
        """
        Метод преобразования данных вакансии в словарь
        :return: готовый словарь
        """

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
        return (f'Вакансия: {self.name}\n'
                f'Возможная З/П: {self.salary}\n'
                f'Формат работы: {self.schedule}\n'
                f'Краткое описание: {self.description}\n'
                f'Краткие требования: {self.requirements}\n'
                f'url: {self.url}\n\n')

    @classmethod
    def cast_to_object_list(cls, sorted_list):
        """
        Классовый метод создания экземпляров класса Vacancy по получаемому списку словарей
        :param sorted_list: список словарей вакансий
        :return: список экземпляров класса Vacancy
        """
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
