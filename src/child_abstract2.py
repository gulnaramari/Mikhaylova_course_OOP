import json
from pathlib import Path
from typing import Dict, List

from config import path_to_testdata_json
from src.abstract2 import JsonEdit
from src.vacancy_validation import VacancyValid


class VacancyManager(JsonEdit):
    """Дочерний класс для работы с файлами, который позволит сохранять вакансии, читать их и удалять.
    Реализуем его для работы с JSON."""
    all_vacancies: list = []

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.save_data([])  # пустой JSON

    def load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []
        except FileNotFoundError:
            return []

    def save_data(self, data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancies: List[VacancyValid]):
        data = self.load_data()
        for vacancy in vacancies:
            data.append(vacancy.to_dict())
        self.save_data(data)

    def filter_vacancies(self, criteria: Dict):
        data = self.load_data()
        result = []
        for item in data:
            if all(item.get(key) == value for key, value in criteria.items()):
                result.append(item)
        return result

    def delete_data(self, criteria: Dict):
        data = self.load_data()
        data = [item for item in data if not all(item.get(key) == value for key, value in criteria.items())]
        self.save_data(data)


if __name__ == "__main__":
    storage = VacancyManager(path_to_testdata_json)
    print(storage.file_path)

    # Очистим файл перед тестом
    storage.save_data([])

    # Добавляем несколько вакансий
    vacancy1 = VacancyValid("Python Developer", "https://example.com/1", 100000, 120000, "Разработка приложений")
    vacancy2 = VacancyValid("Data Scientist", "https://example.com/2", 150000, 200000, "Анализ данных")
    vacancy3 = VacancyValid("Python Developer", "https://example.com/3", 130000, 150000, "Работа с данными")

    storage.add_vacancies([vacancy1, vacancy2, vacancy3])
    print("Вакансии добавлены.")

    # Проверяем get_vacancies без критериев
    print("\nВсе вакансии:")
    print(storage.filter_vacancies({}))

    # Фильтр по названию
    print("\nВакансии с названием 'Python Developer':")
    print(storage.filter_vacancies({"name": "Python Developer"}))

    # Фильтр по зарплате
    print("\nВакансии с зарплатой от 150000:")
    print(storage.filter_vacancies({"salary_from": 150000}))

    # Фильтр по URL
    print("\nВакансия с URL 'https://example.com/2':")
    print(storage.filter_vacancies({"url": "https://example.com/2"}))

    # Удаляем вакансию 'Python Developer'
    storage.delete_data({"name": "Python Developer"})
    print("\nПосле удаления вакансии 'Python Developer':")
    print(storage.filter_vacancies({}))

    # Удаляем вакансию 'Data Scientist'
    storage.delete_data({"name": "Data Scientist"})
    print("\nПосле удаления вакансии 'Data Scientist':")
    print(storage.filter_vacancies({}))

    # Пытаемся удалить несуществующую вакансию
    storage.delete_data({"name": "Frontend Developer"})
    print("\nПосле попытки удаления несуществующей вакансии 'Frontend Developer':")
    print(storage.filter_vacancies({}))

    # Очистим файл перед тестом
    storage.save_data([])

    # Добавляем несколько вакансий
    vacancy1 = VacancyValid("Python Developer", "https://example.com/1", 100000, 120000, "Разработка приложений")
    vacancy2 = VacancyValid("Data Scientist", "https://example.com/2", 150000, 200000, "Анализ данных")
    vacancy3 = VacancyValid("Python Developer", "https://example.com/3", 130000, 150000, "Работа с данными")

    storage.add_vacancies([vacancy1, vacancy2, vacancy3])
    print("Вакансии добавлены.")
