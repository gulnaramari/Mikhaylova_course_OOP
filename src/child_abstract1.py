from abc import ABC
from typing import List
import requests
from src.abstract_1 import ApiJob


class HH(ApiJob):
    """Kласс для работы с API HeadHunter.Класс является дочерним классом от класса ApiJob"""

    def __init__(self, base_url="https://api.hh.ru/vacancies"):
        self.__base_url = base_url

    def get_connecting(self) -> bool:
        """Метод проверки API"""
        response1 = requests.get(self.__base_url)
        if response1.status_code == 200:
            return True
        else:
            raise Exception(f"Failed to connect. Status code={response1.status_code}")

    def get_vacancies(self, search_query: str, page: int = 1, per_page: int = 1) -> List:
        """Преобразование ответа с API в Python объект"""
        __params = {"text": search_query, "page": page, "per_page": per_page}
        response1 = requests.get(self.__base_url, params=__params)

        if response1.status_code == 200:
            return response1.json()["items"]
        else:
            print(f"Ошибка получения данных: {response1.status_code}")
            return []


if __name__ == "__main__":  # pragma: no cover
    response = requests.get("https://api.hh.ru/vacancies", {"text": "python", "page": 0, "per_page": 20})
    print(response.json()["items"])
