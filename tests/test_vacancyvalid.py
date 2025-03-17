import pytest
from src.vacancy_validation import VacancyValid


def test_vacancy_init(vacancy_python):
    """Тестирую создание объекта Vacancy"""
    assert vacancy_python.name == "Python_developer"
    assert (
        vacancy_python.url
        == "https://hh.ru/applicant/vacancy_response?vacancyId=117286365"
    )
    assert vacancy_python.salary_from == 100000
    assert vacancy_python.salary_to == 120000
    assert (
        vacancy_python.description
        == "Разработка и поддержка, back end части веб-приложений."
    )


def test_create_vacancy_without_name(vacancy_without_name):
    """Тест на создание вакансии с отсутствием названия."""
    with pytest.raises(ValueError, match="Название вакансии и URL обязательны."):
        VacancyValid(**vacancy_without_name)


def test_create_vacancy_without_url(vacancy_without_url):
    """Тест на создание вакансии с отсутствием названия."""
    with pytest.raises(ValueError, match="Название вакансии и URL обязательны."):
        VacancyValid(**vacancy_without_url)


def test_create_vacancy_negative_salary(vacancy_with_negative_salary):
    """Тест на создание вакансии с отрицательной зарплатой."""
    with pytest.raises(ValueError, match="Зарплата не может быть меньше 0."):
        VacancyValid(**vacancy_with_negative_salary)


def test_str_method(vacancy_python):
    """Тест на метод __str__."""
    assert (
        str(vacancy_python) == "Вакансия: Python_developer, Зарплата: 100000-120000,"
        " URL: https://hh.ru/applicant/vacancy_response?vacancyId=117286365"
    )


def test_vacancy_comparison_lt(vacancy_python, vacancy_sysadmin):
    """Тест на сравнение вакансий по средней зарплате (меньше)."""
    assert vacancy_python > vacancy_sysadmin


def test_vacancy_comparison_gt(vacancy_sysadmin, vacancy_python):
    """Тест на сравнение вакансий по средней зарплате (больше)."""
    assert vacancy_sysadmin < vacancy_python


def test_from_hh(platform_data):
    """Тест на метод from_hh"""
    vacancies = VacancyValid.from_hh(platform_data)
    # Проверяем количество созданных вакансий
    assert len(vacancies) == 2
    # Проверяем тип объектов
    for vacancy in vacancies:
        assert isinstance(vacancy, VacancyValid)
    # Проверяем данные первой вакансии
    assert vacancies[0].name == "Программист"
    assert vacancies[0].url == "https://example.com/job1"
    assert vacancies[0].salary_from == 80000
    assert vacancies[0].salary_to == 150000
    assert vacancies[0].description == "Отдел разработки"
    # Проверяем данные второй вакансии
    assert vacancies[1].name == "Тестировщик"
    assert vacancies[1].url == "https://example.com/job2"
    assert vacancies[1].salary_from == 60000
    assert vacancies[1].salary_to == 100000
    assert vacancies[1].description == "Отдел тестирования"


def test_vacancy_capsys(capsys, vacancy_python):
    """Тест метода __str__ класса Vacancy с использованием capsys."""
    print(vacancy_python)
    captured = capsys.readouterr()
    expected_output = (
        "Вакансия: Python_developer, Зарплата: 100000-120000,"
        " URL: https://hh.ru/applicant/vacancy_response?vacancyId=117286365\n"
    )
    assert captured.out == expected_output


def test_vacancy_compare(vacancy_python, vacancy_sysadmin):
    """Тест оператора < (__lt__) для сравнения вакансий по средней зарплате."""
    assert vacancy_sysadmin < vacancy_python
    assert not vacancy_python < vacancy_sysadmin


def test_invalid_salary():
    with pytest.raises(ValueError, match="Зарплата не может быть меньше 0."):
        VacancyValid(
            name="Программист Python",
            url="https://example.com",
            salary_from=-100000,
            salary_to=100000,
            description="Разработка приложений",
        )
