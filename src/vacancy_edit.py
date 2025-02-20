import json
from abc import ABC, abstractmethod

class VacancyEdit(ABC):
    @abstractmethod
    def add_vacancy(self, vacancies: List[Vacancy]):
        pass

    @abstractmethod
    def get_vacancy(self, criteria: Dict):
        pass

    @abstractmethod
    def delete_vacancy(self, criteria: Dict):
        pass
