from unittest.mock import patch


def test_hh_api_init(head_hunter_example):
    assert head_hunter_example.base_url == "https://api.hh.ru/vacancies"


def test_connect_success(mock_hh_api):
    """Тест на успешное подключение к API."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        assert mock_hh_api.connect() is True


def test_get_vacancies_success(mock_hh_api):
    """Тест на успешное получение вакансий."""
    with patch("requests.get") as mock_get:
        # Мокаем успешный ответ от API с вакансией
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"items": [{"id": 1, "name": "Developer"}]}
        vacancies = mock_hh_api.get_vacancies("developer")
        assert len(vacancies) == 1
        assert vacancies[0]["name"] == "Developer"


def test_get_vacancies_failure(mock_hh_api):
    """Тест на неудачное получение вакансий."""
    with patch("requests.get") as mock_get:
        # Мокаем неудачный ответ от API
        mock_get.return_value.status_code = 500
        vacancies = mock_hh_api.get_vacancies("developer")
        assert vacancies == []
