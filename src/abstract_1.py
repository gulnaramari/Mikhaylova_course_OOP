from abc import ABC, abstractmethod


class ApiJob(ABC):
    """Абстрактный класс должен быть интерфейсом для всех платформ, с которых мы будем собирать вакансии. В нем будут
    определены методы, которые необходимо реализовать в каждом конкретном классе-платформе, например, для hh.ru."""

    @abstractmethod
    def get_connecting(self):
        """Метод для подключения к API платформе"""
        pass

    @abstractmethod
    def get_vacancies(self, query: str, pages: int, per_page: int):
        """Метод для получения списка вакансий по поисковому запросу"""
        pass
