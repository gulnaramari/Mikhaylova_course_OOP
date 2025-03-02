from unittest.mock import patch


def test_connect_success(head_hunter_example):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        assert head_hunter_example._HH__base_url == "https://api.hh.ru/vacancies"


def test_connect_failure(mock_hh_api):
    """Тест на ошибку подключения к API."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        assert mock_hh_api.get_connecting() is False


def test_get_vacancies_success(mock_hh_api):
    """Тест на успешное получение вакансий."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "items": [{"id": 1, "name": "Developer"}]
        }
        vacancies = mock_hh_api.get_vacancies("Developer")
        assert len(vacancies) == 1
        assert vacancies[0]["name"] == "Developer"


def test_get_vacancies_failure(mock_hh_api):
    """Тест на неудачное получение вакансий."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        vacancies = mock_hh_api.get_vacancies("Developer")
        assert vacancies == []
