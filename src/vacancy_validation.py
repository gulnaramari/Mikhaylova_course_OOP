from typing import Dict, List


"""Класс, который будет представлять вакансию с атрибутами,
 такими как название, ссылка, зарплата, описание,краткое описание или требования
 (всего не менее четырех атрибутов). Класс должен поддерживать
 методы сравнения вакансий между собой по зарплате
и валидировать данные, которыми инициализируются его атрибуты"""

class VacancyValidate:
    __slots__ = ["name", "url", "salary_min", "salary_max", "description"]

    def __init__(self, name, url, salary_min=None, salary_max=None, description=None) -> None:
        self.name = name
        self.url = url
        self.salary_min = salary_min if salary_min else 0
        self.salary_max = salary_max if salary_max else 0
        self.description = description or "Описание не указано"

        self.validation()

