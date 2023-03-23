import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose your language")


@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("language")
    browser = None
    if browser_name:
        print("\nstart ru-version of site..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': f'{browser_name}, en'})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru/en or something different")

    yield browser
    print("\nquit browser..")
    browser.quit()


