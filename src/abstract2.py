from typing import Dict, List
from abc import ABC, abstractmethod
from src.vacancy_validation import VacancyValid

class JsonEdit(ABC):
    """Абстрактный класс для работы с файлами, который позволит сохранять вакансии, читать их и удалять.
    Реализуем его для работы с JSON."""
    @abstractmethod
    def add_vacancy(self, vacancies: List[VacancyValid]):
        pass

    @abstractmethod
    def get_vacancy(self, criteria: Dict):
        pass

    @abstractmethod
    def delete_vacancy(self, criteria: Dict):
        pass
