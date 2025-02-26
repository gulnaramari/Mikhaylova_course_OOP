import json
from pathlib import Path
from typing import Dict, List
from src.abstract2 import JsonEdit
from src.vacancy_validation import VacancyValid


class VacancyManager(JsonEdit):
    def __init__(self, file_path: str = "vacancies.json") -> None:
        self.__file_path = Path(file_path)
        if not self.__file_path.exists():
            self.__save_data([])

    def __get_data(self) -> List[Dict]:
        """Приватный метод для загрузки данных из JSON-файла."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []

    def __save_data(self, data: List[Dict]) -> None:
        """Приватный метод для сохранения данных в JSON-файл."""
        try:
            with open(self.__file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")

    def add_vacancies(self, vacancies: List[VacancyValid]) -> None:
        """Добавляет список вакансий в JSON - файл, проверяем дублирование."""
        data = self.__load_data()
        for vacancy in vacancies:
            vacancy_dict = vacancy.to_dict()
            if vacancy_dict not in data:
                data.append(vacancy_dict)
        self.__save_data(data)

    def get_vacancies(self, criteria: Dict) -> List[Dict]:
        """Возвращает список вакансий, которые соответствуют моим критериям."""
        data = self.__load_data()
        result = []
        for item in data:
            if all(item.get(key) == value for key, value in criteria.items()):
                result.append(item)
        return result

    def delete_vacancies(self, criteria: Dict) -> None:
        """Удаляет вакансии, соответствующие моим критериям, из JSON-файла."""
        data = self.__load_data()
        data = [item for item in data
                if not all(item.get(key) == value for key, value in criteria.items())]
        self.__save_data(data)
