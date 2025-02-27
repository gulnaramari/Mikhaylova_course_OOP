from abc import ABC
from typing import Dict, List, Optional
import requests
from src.abstract_1 import ApiJob


class HH(ApiJob, ABC):
    """Kласс для работы с API HeadHunter.
     Класс является дочерним классом от класса ApiJob"""
    def __init__(self, __base_url, __headers, __params) -> None:
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": " ", "pages": 2, "per_page": 5}

    def __get_connect(self, query: str,
                      pages: int, per_page: int = 10) -> Optional[requests.Response]:
        """Метод проверки API"""
        self.__params.query = query
        self.__params.pages = pages
        self.__params.per_page = per_page

        try:
            response1 = requests.get(self.__base_url, headers=self.__headers, params= self.__params)
            if response1.status_code==200:
                return response1
            else:
                raise Exception(f"Failed to connect. Status code={response1.status_code}")

        except Exception as e:
            print(f"Error: {e}")
            return False


    def get_vacancy(self, query: str, pages: int, per_page: int) -> List:
        """Получаем вакансии с платформы hh.ru по заданному запросу и количеству на страницу."""
        list_vac = []
        for page in range(pages):
            response = self.__get_connect(query, pages, per_page)
            if response:
                vacancies = response.json().get("items", [])
                list_vac.extend(vacancies)
        return list_vac


if __name__ == "__main__":
    hh_url = url.base_url
    print(hh_url)

    response = url.get_vacancy("Электрик", 12, 3)
    print(response)
    status = response.status_code
    result = response.text
    print(status)
    print(result)


