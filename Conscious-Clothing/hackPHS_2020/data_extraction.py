import requests
from bs4 import BeautifulSoup


def data_parser(url):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    product_data = soup.find(attrs={'a-unordered-list a-vertical a-spacing-mini'}).get_text()
    product_data = product_data.replace("\n", " ")
    product_data = product_data.split()

    return product_data;