from typing import Dict, List
from pandas import DataFrame


class VacancyValid:
    __slots__ = ["name", "url", "salary_from", "salary_to", "description"]
    """Класс, который будет представлять вакансию с атрибутами, такими как название, ссылка, зарплата, описание,
    а также методы для сравнения вакансий по зарплате и валидации данных."""

    dataset: dict
    df_categories: DataFrame

    def __init__(
            self, name, url, salary_from=None, salary_to=None, description=None
    ) -> None:
        self.name = name
        self.url = url
        self.salary_from = salary_from if salary_from is not None else 0
        self.salary_to = salary_to if salary_to is not None else 0
        self.description = description or "Описание не указано"

        # Валидация данных
        self.__validate()

    def __validate(self) -> None:
        """Приватный метод для валидации по зарплате"""
        if not self.name or not self.url:
            raise ValueError("Название вакансии и URL обязательны.")
        if self.salary_from < 0 or self.salary_to < 0:
            raise ValueError("Зарплата не может быть меньше 0.")

    def __str__(self) -> str:
        """Возвращает строковое представление объекта VacancyValid."""
        return f"Вакансия: {self.name}, Зарплата: {self.salary_from}-{self.salary_to}, URL: {self.url}"

    def __lt__(self, other) -> bool:
        """Сравнение вакансий по минимальной зарплате"""
        return (self.salary_from + self.salary_to) / 2 < (
                other.salary_from + other.salary_to
        ) / 2

    def __gt__(self, other) -> bool:
        """Сравнение вакансий по максимальной зарплате"""
        return (self.salary_from + self.salary_to) / 2 > (
                other.salary_from + other.salary_to
        ) / 2

    @staticmethod
    def from_dict(data_: List[Dict]) -> List:
        """Метод для формирования списка вакансий из данных платформы"""
        vac = []
        for vac_data in data_:
            name = vac_data.get("name", "Название не указано")
            url = vac_data.get("apply_alternate_url", "")

            salary_from = (
                vac_data.get("salary", {}).get("from", 0)
                if vac_data.get("salary")
                else 0
            )
            salary_to = (
                vac_data.get("salary", {}).get("to", 0) if vac_data.get("salary") else 0
            )

            department = vac_data.get("department")
            description = (
                department.get("name", "Описание не указано")
                if department
                else "Описание не указано"
            )

            vacancy_ = VacancyValid(
                name=name,
                url=url,
                salary_from=salary_from,
                salary_to=salary_to,
                description=description,
            )
            vac.append(vacancy_)
        return vac

    def to_dict(self) -> Dict:
        """Преобразует экземпляр класса VacancyValid в словарь"""
        return {
            "name": self.name,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
        }


if __name__ == "__main__":  # pragma: no cover
    vacancy_developer = VacancyValid(
        name="Python_developer",
        url="https://hh.ru/applicant/vacancy_response?vacancyId=117286365",
        salary_from=100000,
        salary_to=120000,
        description="Разработка и поддержка, back end части веб-приложений."
    )
    print(vacancy_developer.__str__())
    print(vacancy_developer.to_dict())
