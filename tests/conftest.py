import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Инициализация драйвера перед тестом
    browser = webdriver.Chrome()
    browser.get("https://qa-desk.education-services.ru/")
    
    yield browser
    
    # Закрытие браузера после теста (соответствует требованиям autonomity и driver.quit())
    browser.quit()