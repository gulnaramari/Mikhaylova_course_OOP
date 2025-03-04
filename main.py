from config import path_to_data_json
from src.child_abstract2 import VacancyManager
from src.child_abstract1 import HH
import pandas as pd


if __name__ == "__main__":
    vacancy = input('Введите название вакансии')
    top_n_vacancy = int(input('Введите количество вакансий'))

    # блок работы с HeadHunterAPI
    hh_vacancies = HH('https://api.hh.ru/vacancies')
    vacancies = hh_vacancies.get_vacancies('python', 2, 20)
    print(vacancies)

    # блок работы с файлом
    vacancies_work = VacancyManager(path_to_data_json)
    vacancies_work.save_data(vacancies)  # добавляем в файл
    vacancies_work.read_data(vacancies)  # формируем объекты для класса VacancyValid

    is_sorting = input("Хотите отсортировать вакансии? (Y/N): ")
    if is_sorting.lower() == 'y':
        sorting_direction = input("Сортировка будет по возрастанию или убыванию? (ASC/DESC): ")
        if sorting_direction.lower() == 'desc':
            reverse = True
        else:
            reverse = False
        [print(v) for v in sorted(vacancies_work.all_vacancies, reverse=reverse)]
    else:
        print("Вакансии не отсортированы")

    # найти топ n вакансий
    is_top_n_vacancy = input(f'Вывести топ {top_n_vacancy} вакансий? (Y/N):')
    if is_top_n_vacancy.lower() == 'y':
        df = pd.DataFrame(vacancies_work.all_vacancies)
        print(df.head(top_n_vacancy))
    else:
        print('Вакансии не выведены.')
