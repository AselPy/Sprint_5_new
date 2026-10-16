from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestAdvertisement:

    def test_create_advertisement_unauthorized(self):
        driver = webdriver.Chrome()
        try:
            driver.get("https://qa-desk.education-services.ru/")
            wait = WebDriverWait(driver, 15)

            wait.until(
                EC.element_to_be_clickable(
                    Locators.BTN_ADD_ADVERTISEMENT
                )
            ).click()

            modal = wait.until(
                EC.visibility_of_element_located(
                    Locators.MODAL_TITLE_UNAUTHORIZED
                )
            )

            assert modal.is_displayed()
        finally:
            driver.quit()

    def test_create_advertisement_authorized(self):
        # Временно проверяем только запуск браузера и открытие сайта.
        driver = webdriver.Chrome()
        try:
            driver.get("https://qa-desk.education-services.ru/")
            assert driver.title == "React App"
        finally:
            driver.quit()