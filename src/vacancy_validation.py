from src.child_abstract1 import HH


class VacancyValid:
    __slots__ = ["name", "url", "salary_from", "salary_to", "description"]
    """Класс, который будет представлять вакансию с атрибутами, такими как название, ссылка, зарплата, описание,
    а также методы для сравнения вакансий по зарплате и валидации данных."""

    def __init__(self, name, url, salary_from, salary_to, description) -> None:
        self.name = name
        self.url = url
        self.salary_from = salary_from if salary_from is not None else 0
        self.salary_to = salary_to if salary_to is not None else 0
        self.description = description or "Описание не указано"
        self.validate()

    def validate(self):
        """Метод для валидации данных вакансии"""
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
    def from_hh(data):
        """Метод для формирования списка вакансий из данных платформы"""
        vacancies_fromhh = []
        for vac in data:
            name = vac.get("name", "Название не указано")
            url = vac.get("url", "")
            salary_from = (
                vac.get("salary", {}).get("from", 0) if vac.get("salary") else 0
            )
            salary_to = vac.get("salary", {}).get("to", 0) if vac.get("salary") else 0
            department = vac.get("department")
            description = (
                department.get("name", "Описание не указано")
                if department
                else "Описание не указано"
            )

            vacancy1 = VacancyValid(
                name=name,
                url=url,
                salary_from=salary_from,
                salary_to=salary_to,
                description=description,
            )

            vacancies_fromhh.append(vacancy1)
        return vacancies_fromhh

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
        }


if __name__ == "__main__":
    platform = HH("https://api.hh.ru/vacancies")

    if platform.get_connecting():
        platform_data = platform.get_vacancies("сантехник")
        vacancies = VacancyValid.from_hh(platform_data)
        for vacancy in vacancies:
            print(vacancy)
        print(vacancies)
