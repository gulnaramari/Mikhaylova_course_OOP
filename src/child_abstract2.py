import json
from pathlib import Path
from typing import Dict, List
from src.abstract2 import JsonEdit
from src.vacancy_validation import VacancyValid


class VacancyManager(JsonEdit):
    """Дочерний класс для работы с файлами, который позволит сохранять вакансии, читать их и удалять.
    Реализуем его для работы с JSON."""
    all_vacancies: list = []

    def __init__(self, file_path):
        self.__file_path = Path(file_path)
        if not self.__file_path.exists():
            self.save_data([])

    def save_data(self, vacancies: list[dict]):
        """ Сохраняет данные формата json(список словарей) в файл"""
        try:
            with open(self.__file_path, 'w', encoding='utf-8') as json_file:
                json.dump(vacancies, json_file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")
            return []

    def read_data(self, vacancies: list[dict]):
        """ Читает json файл и добавляет вакансии """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            vacancies = []
            for vacancy in data:
                vacancies.append(VacancyValid(
                    vacancy['name'],
                    vacancy['url'],
                    vacancy['salary_from'],
                    vacancy['salary_to'],
                    vacancy['description']))
                self.all_vacancies = vacancies
        except FileNotFoundError:
            print(f"Файл {self.__file_path} не найден.")
            self.all_vacancies = []

    @classmethod
    def return_vacancies(cls):
        """ чтение json файла """
        return cls.all_vacancies

    def delete_data(self):
        """ Удаляет данные из файла """
        with open(self.__file_path, 'w'):
            pass

    def __str__(self):
        return str(getattr(self, 'all_vacancies', ''))


if __name__ == "__main__":  # pragma: no cover
    vacancy1 = VacancyValid("Python Developer", "https://example.com/1", 100000, 120000, "Разработка приложений")
    vacancy2 = VacancyValid("Data Scientist", "https://example.com/2", 150000, 200000, "Анализ данных")
    vacancy3 = VacancyValid("Python Developer", "https://example.com/3", 130000, 150000, "Работа с данными")
    storage = [vacancy1, vacancy2, vacancy3]
    print(vacancy1.name)
    print(vacancy2.name)
    print(vacancy3.name)

    print("Вакансии добавлены.")

