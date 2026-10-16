import random
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestRegistration:
    URL = "https://qa-desk.education-services.ru/"

    def open_registration(self, driver):
        """Вспомогательный метод для открытия формы регистрации."""
        wait = WebDriverWait(driver, 15)

        # 1. Открываем модальное окно входа
        wait.until(
            EC.element_to_be_clickable(Locators.BTN_ENTER_REG)
        ).click()
        time.sleep(0.5)

        # 2. Пытаемся переключиться на форму регистрации, если она еще не открыта
        try:
            wait.until(
                EC.element_to_be_clickable(Locators.BTN_NO_ACCOUNT)
            ).click()
            time.sleep(0.5)
        except Exception:
            pass

        # 3. Возвращаем объект ожидания и найденное поле email
        email_field = wait.until(
            EC.visibility_of_element_located(Locators.INPUT_EMAIL)
        )
        return wait, email_field

    def test_successful_registration(self):
        driver = webdriver.Chrome()
        try:
            driver.get(self.URL)
            wait, email_field = self.open_registration(driver)

            unique_email = f"user_{random.randint(1000, 9999)}@example.com"
            password = "TestPassword123!"

            email_field.send_keys(unique_email)
            driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
            driver.find_element(*Locators.INPUT_PASSWORD_CONFIRM).send_keys(password)
            driver.find_element(*Locators.BTN_CREATE_ACCOUNT).click()

            logout_btn = wait.until(
                EC.visibility_of_element_located(Locators.BTN_LOGOUT)
            )
            assert logout_btn.is_displayed()

        finally:
            driver.quit()

    def test_registration_invalid_email_format(self):
        driver = webdriver.Chrome()
        try:
            driver.get(self.URL)
            wait, email_field = self.open_registration(driver)

            email_field.send_keys("incorrect_email_format")
            driver.find_element(*Locators.BTN_CREATE_ACCOUNT).click()

            error_element = wait.until(
                EC.visibility_of_element_located(Locators.ERROR_MESSAGE)
            )
            assert error_element.is_displayed()

        finally:
            driver.quit()

    def test_registration_existing_user(self):
        driver = webdriver.Chrome()
        try:
            driver.get(self.URL)
            wait, email_field = self.open_registration(driver)

            unique_email = f"existing_{random.randint(1000, 9999)}@example.com"
            password = "TestPassword123!"

            # 1. Первая регистрация
            email_field.send_keys(unique_email)
            driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
            driver.find_element(*Locators.INPUT_PASSWORD_CONFIRM).send_keys(password)
            driver.find_element(*Locators.BTN_CREATE_ACCOUNT).click()

            wait.until(
                EC.visibility_of_element_located(Locators.BTN_LOGOUT)
            )
        finally:
            driver.quit()

        # 2. Повторная попытка регистрации с тем же email
        driver = webdriver.Chrome()
        try:
            driver.get(self.URL)
            wait, email_field = self.open_registration(driver)

            email_field.send_keys(unique_email)
            driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
            driver.find_element(*Locators.INPUT_PASSWORD_CONFIRM).send_keys(password)
            driver.find_element(*Locators.BTN_CREATE_ACCOUNT).click()

            error_element = wait.until(
                EC.visibility_of_element_located(Locators.ERROR_MESSAGE)
            )
            assert error_element.is_displayed()

        finally:
            driver.quit()