from src.child_abstract2 import VacancyManager
from src.child_abstract1 import HH
from src.vacancy_validation import VacancyValid
from pathlib import Path

def user_interaction():
    """Функция для взаимодействия с пользователем через консоль, которая будет запрашивать данные,
    отображать результаты и позволять фильтровать вакансии."""

    platform = HH()
    storage = VacancyManager()

    if not platform.get_connecting():
        print("Не удалось подключиться к API hh.ru")
        return
    while True:
        print("\n1. Ввести поисковый запрос")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Найти вакансии по ключевому слову в описании")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            query = input("Введите поисковый запрос: ")
            data_ = platform.get_vacancies(query)
            vacancies_list = VacancyValid.from_dict(data_)
            storage.add_vacancy(vacancies_list)
            for vacancy in vacancies_list:
                print(vacancy)

        elif choice == "2":
            n = int(input("Сколько вакансий вывести?: "))
            data = storage.load_data()

            sorted_vacancies = sorted(
                data,
                key=lambda x: (x["salary_from"] + x["salary_to"]) / 2,
                reverse=True,
            )
            for vacancy in sorted_vacancies[:n]:
                print(vacancy)

        elif choice == "3":
            keyword = input("Введите ключевое слово: ")
            data = storage.load_data()

            filtered = [v for v in data if keyword.lower() in v["description"].lower()]
            for vacancy in filtered:
                print(vacancy)
        elif choice == "4":
            break

        else:
            print("Неверный выбор, попробуйте снова.")
