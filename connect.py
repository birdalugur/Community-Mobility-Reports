import requests
import bs4
from time import sleep


def connect(url: str) -> requests.Response:
    done = False
    while not done:
        try:
            r = requests.get(url)
            done = True
            print(f'connection successful for {url}')
        except requests.exceptions.ConnectionError:
            status_code = "Connection refused"
            sleep(3)
            print(status_code, url)
    return r


def get_content(url: str) -> bs4.BeautifulSoup:
    page = connect(url)
    return bs4.BeautifulSoup(page.content, "html.parser")
