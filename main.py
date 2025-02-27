from src.child_abstract2 import VacancyManager
from src.child_abstract1 import HH
from src.vacancy_validation import VacancyValid

def user_interaction():
    """Функция для взаимодействия с пользователем через консоль, которая будет запрашивать данные,
     отображать результаты и позволять фильтровать вакансии."""

    hh_platform = HH()
    if not hh_platform.connect():
        return

    storage = VacancyManager('vacancies.json')

    while True:
        print("\nМеню:")
        print("1. Поиск вакансий")
        print("2. Топ N вакансий по зарплате")
        print("3. Вакансии с ключевым словом в описании")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            search_query = input("Введите поисковый запрос: ")
            vacancies = hh_platform.get_vacancies(search_query)
            for vacancy in vacancies:
                v = VacancyValid(vacancy["name"], vacancy["url"],
                                 vacancy["salary_from"], vacancy["salary_to"],
                                 vacancy["description"])
                storage.add_vacancy(v)
            print(f"Найдено {len(vacancies)} вакансий.")
        elif choice == "2":
            N = int(input("Введите количество вакансий для отображения: "))
            vacancies = storage.get_vacancies("")
            vacancies.sort(reverse=True)
            for v in vacancies[:N]:
                print(v)
        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска в описаниях: ")
            vacancies = storage.get_vacancies(keyword)
            for v in vacancies:
                print(v)
        elif choice == "4":
            break

