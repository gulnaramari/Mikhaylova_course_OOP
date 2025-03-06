def filter_vac(data, keyword):
    matched_vacancies = []
    for vac in data:
        for key, value in vac.items():
            if keyword.lower() in str(value).lower():
                matched_vacancies.append(vac)
                break

    for vacancy in matched_vacancies:
        print(vacancy)


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция сортирует вакансии по вилке зарплаты (от и до)"""
    if filtered_vacancies is None:
        print("Ошибка: filtered_vacancies не должно быть None.")
        return []

    filtered_salary_vacancies = []
    from_to_salary = salary_range.split()

    try:
        min_salary = int(from_to_salary[0])
        max_salary = int(from_to_salary[2])
    except (IndexError, ValueError):
        print("Некорректный ввод диапазона зарплат. Пример: '100000 - 150000'")
        return []

    for vacancy in filtered_vacancies:
        salary = vacancy.get("salary", {})

        # Check if salary is None or not a dictionary
        if salary is None or not isinstance(salary, dict):
            continue

        salary_from = salary.get("from")
        salary_to = salary.get("to")

        if salary_from is not None and salary_to is not None:
            try:
                salary_from = int(salary_from)
                salary_to = int(salary_to)
            except ValueError:
                continue

            if salary_from >= min_salary and salary_to <= max_salary:
                filtered_salary_vacancies.append(vacancy)

    return sorted(
        filtered_salary_vacancies,
        key=lambda x: x["salary"].get("to", 0),
        reverse=True
    )

def get_top_vacancies(filtered_vacancies, n_vac):
    """Функция вывода топ вакансий по выбору пользователя"""
    filtered_vacancies = filtered_vacancies[0: n_vac]
    return filtered_vacancies

