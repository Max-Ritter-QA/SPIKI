import allure
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-insecure-localhost')
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()