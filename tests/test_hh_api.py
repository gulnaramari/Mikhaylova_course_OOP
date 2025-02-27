from unittest.mock import patch


def test_hh_api_init(head_hunter_example):
    assert head_hunter_example.base_url == "https://api.hh.ru/vacancies"


def test_connect_success(mock_hh_api):
    """Тест на успешное подключение к API."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        assert mock_hh_api.connect() is True
