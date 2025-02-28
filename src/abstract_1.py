from abc import ABC, abstractmethod



class ApiJob(ABC):
    """Абстрактный класс должен быть интерфейсом для всех платформ, с которых мы будем собирать вакансии. В нем будут
    определены методы, которые необходимо реализовать в каждом конкретном классе-платформе, например, для hh.ru."""

    @abstractmethod
    def __get_connect(self):
        """Метод для подключения к API платформе"""
        pass

    @abstractmethod
    def __get_vacancy(self, query: str, page: int = 1):
        """Метод для получения списка вакансий по поисковому запросу"""
        pass

