import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose laguage: ru or en")


@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("language")
    browser = None
    if browser_name == "ru":
        print("\nstart ru-version of site..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru, en'})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "en":
        print("\nstart en-version of site..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en, ru'})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru or en")

    yield browser
    print("\nquit browser..")
    browser.quit()


