from typing import Dict, List


class VacancyValidate:
    """Класс, который будет представлять вакансию с атрибутами,
     такими как название, ссылка, зарплата, описание,краткое описание или требования
     (всего не менее четырех атрибутов). Класс должен поддерживать
     методы сравнения вакансий между собой по зарплате
    и валидировать данные, которыми инициализируются его атрибуты"""

    __slots__ = ["name", "url", "salary_min", "salary_max", "description"]

    def __init__(self, name, url, salary_min=None, salary_max=None, description=None) -> None:
        self.name = name
        self.url = url
        self.salary_min = salary_min if salary_min else 0
        self.salary_max = salary_max if salary_max else 0
        self.description = description or "Описание не указано"

        self.validation()

    def __validate(self) -> None:
        """Приватный метод для валидации данных вакансии"""
        if not self.name or not self.url:
            raise ValueError("Название вакансии и URL обязательны.")
        elif self.salary_min < 0:
            raise ValueError("Минимальное значение зарплаты не может быть меньше 0.")
        elif self.salary_max > self.salary_min:
            raise ValueError("Минимальное значение зарплатной вилки"
                             " не может быть больше ее максимального значения")

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Vacancy."""
        return f"Вакансия: {self.name}," \
               f" зарплатная вилка: {self.salary_min}-{self.salary_max}," \
               f" URL: {self.url}"

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по минимальной зарплате"""
        return self.salary_min < other.salary_min

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по максимальной зарплате"""
        return (self.salary_min + self.salary_max) / 2 > (other.salary_min + other.salary_max) / 2

    @staticmethod
    def from_hh(api_data: List[Dict]) -> List:
        """Метод для формирования списка вакансий из api-данных hh.ru"""
        vacancies = []
        for vac in api_data:
            name = vac.get("name", "Название не указано")
            url = vac.get("apply_alternate_url", "")
            salary_min = vac.get("salary", {}).get("from", 0) if vac.get("salary") else 0
            salary_max = vac.get("salary", {}).get("to", 0) if vac.get("salary") else 0

            department = vac.get("department")
            description = department.get("name", "Описание не указано")\
                if department else "Описание не указано"

            vacancy = VacancyValidate(
                name=name, url=url, salary_min=salary_min,
                salary_max=salary_max, description=description
            )
            vacancies.append(vacancy)
        return vacancies


    def to_dict(self) -> Dict:
        """Преобразует экземпляр класса VacancyValidate в словарь"""
        return {
            "name": self.name,
            "url": self.url,
            "salary_min": self.salary_min,
            "salary_max": self.salary_max,
            "description": self.description,
        }
