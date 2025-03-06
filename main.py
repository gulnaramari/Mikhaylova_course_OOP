from pprint import pprint

from config import path_to_data_json
from src.child_abstract2 import VacancyManager
from src.child_abstract1 import HH
import pandas as pd
from src.user_interaction import filter_vac, get_vacancies_by_salary, get_top_vacancies
from src.vacancy_validation import VacancyValid

if __name__ == "__main__":
    mydata = VacancyManager(path_to_data_json)
    vacancy = input('Введите поисковый запрос:')
    n_vacancy = int(input('Введите количество вакансий'))
    # блок работы с HeadHunterAPI
    hh_vacancies = HH('https://api.hh.ru/vacancies')
    vacancies = hh_vacancies.get_vacancies(vacancy, 10, n_vacancy)
    pprint(vacancies)
    vacancies_list = VacancyValid.from_hh(vacancies)
    mydata.add_vacancies(vacancies_list)
    print(vacancies_list)

    # блок работы с файлом фильтрация по ключевому слову
    keyword = input("Введите ключевое слово: ")
    data_ = mydata.load_data()
    filtered_vacancies = filter_vac(data_, keyword)

    # блок работы с файлом сортировка по зп
    salary_range = input("Введите диапазон зарплат: ")
    ranged_vacancies = get_vacancies_by_salary(data_, salary_range)
    print(ranged_vacancies)
    # блок работы с файлом получение топовых вакансий
    is_top_n_vacancy = input(f'Вывести топ {n_vacancy} вакансий? (Y/N):')
    if is_top_n_vacancy.lower() == 'y':
        top_vacancies = get_top_vacancies(data_, n_vacancy)
        print(top_vacancies)
    else:
        print('Вакансии не выведены.')

