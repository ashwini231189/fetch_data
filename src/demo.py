"""This file for python code."""

import requests  # pylint: disable=E401
from requests import Response  # pylint: disable=E401


def fetch_demo(url: str) -> Response:
    """Passing URL.

    Args:
        url (str): URL requires to fetch data.

    Returns:
        str: It fetches data.
    """
    return requests.get(url, timeout=10)


fetch_demo("https://api.publicapis.org/entries")
