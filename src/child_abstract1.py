from abc import ABC
from typing import Dict, List, Optional
import requests
from urllib3.util import url

from src.abstract_1 import ApiJob


class HH(ApiJob):
    """Kласс для работы с API HeadHunter.
     Класс является дочерним классом от класса ApiJob"""
    def __init__(self, base_url="https://api.hh.ru/vacancies"):
        self.base_url = base_url

    def get_connecting(self) -> Optional[requests.Response]:
        """Метод проверки API"""
        try:
            response1 = requests.get(self.base_url)
            if response1.status_code==200:
                return response1
            else:
                raise Exception(f"Failed to connect. Status code={response1.status_code}")

        except Exception as e:
            print(f"Error: {e}")
            return False



    def get_vacancies(self, search_query: str) -> List:
        """Получаем вакансии с платформы hh.ru по заданному запросу и количеству на страницу."""
        params = {"text": search_query}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()["items"]
        else:
            print(f"Ошибка получения данных: {response.status_code}")
            return []


