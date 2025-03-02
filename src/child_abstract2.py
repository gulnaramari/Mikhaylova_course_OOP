import json
from pathlib import Path
from typing import Dict, List
from src.abstract2 import JsonEdit
from src.vacancy_validation import VacancyValid


class VacancyManager(JsonEdit):
    """Дочерний класс для работы с файлами, который позволит сохранять вакансии, читать их и удалять.
    Реализуем его для работы с JSON."""

    def __init__(self, file_path) -> None:
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            self.__save_data([])

    def __load_data(self):
        """Приватный метод для загрузки данных из JSON-файла."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []

    def __save_data(self, data):
        """Приватный метод для сохранения данных в JSON-файл."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")

    def add_vacancy(self, vacancies: List[VacancyValid]) -> None:
        """Добавляет список вакансий в JSON - файл, проверяем дублирование."""
        data = self.__load_data()
        for vacancy in vacancies:
            vacancy_dict = vacancy.to_dict()
            if vacancy_dict not in data:
                data.append(vacancy_dict)
        self.__save_data(data)

    def get_vacancy(self, criteria: Dict) -> List[Dict]:
        """Возвращает список вакансий, которые соответствуют моим критериям."""
        data = self.__load_data()
        result = []
        for item in data:
            if all(item.get(key) == value for key, value in criteria.items()):
                result.append(item)
        return result

    def delete_vacancy(self, criteria: Dict):
        """Удаляет вакансии, соответствующие моим критериям, из JSON-файла."""
        data = self.__load_data()
        data = [item for item in data if not all(item.get(key) == value for key, value in criteria.items())]
        self.__save_data(data)


if __name__ == "__main__":
    storage = VacancyManager(
        "C:/Users/Daniel/PycharmProjects/Mother/pythonProject1/data/hh_vacancies.json")
    print(storage.file_path)

    # Очистим файл перед тестом
    storage.delete_vacancy({})

    # Добавляем несколько вакансий
    vacancy1 = VacancyValid("Python Developer", "https://example.com/1", 100000, 120000, "Разработка приложений")
    vacancy2 = VacancyValid("Data Scientist", "https://example.com/2", 150000, 200000, "Анализ данных")
    vacancy3 = VacancyValid("Python Developer", "https://example.com/3", 130000, 150000, "Работа с данными")

    storage.add_vacancy([vacancy1, vacancy2, vacancy3])
    print("Вакансии добавлены.")

    # Проверяем get_vacancies без критериев
    print("\nВсе вакансии:")
    print(storage.get_vacancy({}))

    # Фильтр по названию
    print("\nВакансии с названием 'Python Developer':")
    print(storage.get_vacancy({"name": "Python Developer"}))

    # Фильтр по зарплате
    print("\nВакансии с зарплатой от 150000:")
    print(storage.get_vacancy({"salary_from": 150000}))

    # Фильтр по URL
    print("\nВакансия с URL 'https://example.com/2':")
    print(storage.get_vacancy({"url": "https://example.com/2"}))

    # Удаляем вакансию 'Python Developer'
    storage.delete_vacancy({"name": "Python Developer"})
    print("\nПосле удаления вакансии 'Python Developer':")
    print(storage.get_vacancy({}))

    # Удаляем вакансию 'Data Scientist'
    storage.delete_vacancy({"name": "Data Scientist"})
    print("\nПосле удаления вакансии 'Data Scientist':")
    print(storage.get_vacancy({}))

    # Пытаемся удалить несуществующую вакансию
    storage.delete_vacancy({"name": "Frontend Developer"})
    print("\nПосле попытки удаления несуществующей вакансии 'Frontend Developer':")
    print(storage.get_vacancy({}))
