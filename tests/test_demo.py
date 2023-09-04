"""This python file for test fetch data."""

from src.demo import fetch_data


def test_fetch_data():
    """Test case for check response."""
    response = fetch_data(url="https://api.publicapis.org/entries")
    data = response.json()

    assert response.status_code == 200
    assert data["count"] == 1425
