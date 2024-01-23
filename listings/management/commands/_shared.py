from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_page_contents(link: str):
    req = Request(link)

    html_page = urlopen(req).read()
    return BeautifulSoup(html_page, 'html.parser')