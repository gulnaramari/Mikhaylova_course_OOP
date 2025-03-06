from abc import ABC, abstractmethod
from typing import List, Dict


class JsonEdit(ABC):
    """Абстрактный класс для работы с файлами, который позволит сохранять вакансии, читать их и удалять.
    Реализуем его для работы с JSON."""

    @abstractmethod
    def add_vacancies(self, vacancies: List[Dict]):
        pass

    @abstractmethod
    def filter_vacancies(self, criteria: Dict):
        pass

    @abstractmethod
    def delete_data(self, criteria: Dict):
        pass