"""Fetch method to fetch data."""
import logging
from requests import Response  # pylint: disable=import-error
import requests

logging.basicConfig(
    filename="fetched.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def fetch(url):
    """Pass URL to fetch method."""
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        logging.info("Api call successful for %s", url)
        return response.json()
    return logging.error("wrong url %s", url)


fetch("https://api.agify.io?name=meelad")
