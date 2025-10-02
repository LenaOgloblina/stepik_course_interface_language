import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru, es or en")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name must be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("--language")
    language_code = None
    if language == "ru":
        language_code = "ru"
    elif language == "en-gb":
        language_code = "en-gb"
    elif language == "es":
        language_code = "es"
    elif language == "fr":
        language_code = "fr"
    else:
        raise ValueError("--language must be ru or en")
    return language_code