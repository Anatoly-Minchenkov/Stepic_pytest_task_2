import requests
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
import pytest


def book_grabber():
    page_list = [
        'http://selenium1py.pythonanywhere.com/catalogue/category/books/non-fiction/hacking_7/?page=1',
        'http://selenium1py.pythonanywhere.com/catalogue/category/books/non-fiction/hacking_7/?page=2'
    ]
    shema = 'http://selenium1py.pythonanywhere.com/'
    book_list = []
    for page in page_list:
        response = requests.get(page)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        bufer_book_list = [shema + '/'.join(book_link.find('a')['href'].split('/')[2:]) for
                           book_link in soup.find('section').find_all('h3')]
        book_list += bufer_book_list
    return book_list


book_list = book_grabber()


@pytest.mark.parametrize('book', book_list)
def test_add_item(browser, book):
    browser.get(book)
    old_price = browser.find_element(By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]').text
    browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').click()
    new_price = browser.find_element(By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]').text
    assert old_price != new_price, 'this book dont have "add"-button'
