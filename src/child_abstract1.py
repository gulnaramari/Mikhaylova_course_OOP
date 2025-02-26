from typing import Dict, List, Optional
import requests
from src.abstract_1 import ApiJob


class HH(ApiJob):
    """Kласс для работы с API HeadHunter. Класс ApiJob является родительским классом,
     который необходимо реализовать"""
    def __init__(self, __base_url, __headers, __params) -> None:
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": " ", "pages": 2, "per_page": 5}

    def __get_connect(self, query: str, pages: int, per_page: int = 10) -> Optional[requests.Response]:
        """Метод проверки API"""
        self.__params.query = query
        self.__params.pages = pages
        self.__params.per_page = per_page

        try:
            response = requests.get(self.__base_url, headers=self.__headers, params= self.__params)
            if response.status_code==200:
                return response
            else:
                raise Exception(f"Failed to connect. Status code={response.status_code}")

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
    url = HH(ApiJob).base_url
    response = requests.get(url)
    status = response.status_code
    result = response.text
    print(status)
    print(result)
