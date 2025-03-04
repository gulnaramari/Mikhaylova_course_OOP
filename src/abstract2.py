from typing import Dict, List
from abc import ABC, abstractmethod
from src.vacancy_validation import VacancyValid


class JsonEdit(ABC):
    """Абстрактный класс для работы с файлами, который позволит сохранять вакансии, читать их и удалять.
    Реализуем его для работы с JSON."""

    @abstractmethod
    def save_data(self, vacancies: list[dict]):
        pass


    @abstractmethod
    def read_data(self, vacancies: list[dict]):
        pass


    @abstractmethod
    def delete_data(self):
        pass
