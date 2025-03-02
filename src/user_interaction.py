from src.child_abstract2 import VacancyManager
from src.child_abstract1 import HH
from src.vacancy_validation import VacancyValid


def user_interaction():
    """Функция для взаимодействия с пользователем через консоль, которая будет запрашивать данные,
     отображать результаты и позволять фильтровать вакансии."""

    platform = HH()

    storage = VacancyManager("C:/Users/Daniel/PycharmProjects/Mother/"
                             "pythonProject1/data/hh_vacancies.json")

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
            vacancies = platform.get_vacancies(query)
            vacancies_list = VacancyValid.from_dict(vacancies)
            storage.add_vacancy(vacancies_list)
            print(f"Добавлено {len(vacancies_list)} вакансий.")

        elif choice == "2":
            num = input("Введите ключевое слово: ")
            data = storage.load_data()
            sorted_vacancies = sorted(data, key=lambda x: (x["salary_from"] + x["salary_to"]) / 2, reverse=True)
            for vacancy in sorted_vacancies[:num]:
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


if __name__ == "__main__":
    user_interaction()

