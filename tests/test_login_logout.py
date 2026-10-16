import uuid

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestLoginLogout:

    def register_user(self, driver):
        """Регистрирует нового пользователя и возвращает email и пароль."""
        email = f"user_{uuid.uuid4().hex[:12]}@example.com"
        password = "TestPassword123!"

        wait = WebDriverWait(driver, 15)

        # Открываем окно авторизации
        wait.until(
            EC.element_to_be_clickable(Locators.BTN_ENTER_REG)
        ).click()

        # Переключаемся на регистрацию
        wait.until(
            EC.element_to_be_clickable(Locators.BTN_NO_ACCOUNT)
        ).click()

        # Заполняем email
        wait.until(
            EC.visibility_of_element_located(Locators.INPUT_EMAIL)
        ).send_keys(email)

        # Первое поле пароля
        driver.find_element(
            *Locators.INPUT_PASSWORD
        ).send_keys(password)

        # Подтверждение пароля
        driver.find_element(
            *Locators.INPUT_PASSWORD_CONFIRM
        ).send_keys(password)

        # Создаём аккаунт
        wait.until(
            EC.element_to_be_clickable(Locators.BTN_CREATE_ACCOUNT)
        ).click()

        # Ждём успешной авторизации
        wait.until(
            EC.visibility_of_element_located(Locators.USER_ELEMENT)
        )

        return email, password

    def test_login(self):
        """Проверяет успешную регистрацию и вход пользователя."""
        driver = webdriver.Chrome()

        try:
            driver.get("https://qa-desk.education-services.ru/")

            email, password = self.register_user(driver)

            # Проверяем, что пользователь авторизован
            logout_button = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(Locators.BTN_LOGOUT)
            )

            assert logout_button.is_displayed()
            assert email is not None
            assert password is not None

        finally:
            driver.quit()

    def test_logout(self):
        """Проверяет выход авторизованного пользователя."""
        driver = webdriver.Chrome()

        try:
            driver.get("https://qa-desk.education-services.ru/")

            self.register_user(driver)

            wait = WebDriverWait(driver, 15)

            # Нажимаем кнопку выхода
            wait.until(
                EC.element_to_be_clickable(Locators.BTN_LOGOUT)
            ).click()

            # Ждём исчезновения элемента авторизованного пользователя
            wait.until(
                EC.invisibility_of_element_located(Locators.BTN_LOGOUT)
            )

            # Проверяем возвращение кнопки входа
            login_button = wait.until(
                EC.visibility_of_element_located(Locators.BTN_ENTER_REG)
            )

            assert login_button.is_displayed()

        finally:
            driver.quit()   