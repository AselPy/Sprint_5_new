
from uuid import uuid4

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestLogout:

    def test_logout(self, driver):
        wait = WebDriverWait(driver, 15)

        email = f"logout_{uuid4().hex[:12]}@example.com"
        password = "TestPassword123!"

        # Создаём пользователя и авторизуемся
        wait.until(
            expected_conditions.element_to_be_clickable(
                Locators.BTN_ENTER_REG
            )
        ).click()

        wait.until(
            expected_conditions.element_to_be_clickable(
                Locators.BTN_NO_ACCOUNT
            )
        ).click()

        wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.INPUT_EMAIL
            )
        ).send_keys(email)

        driver.find_element(
            *Locators.INPUT_PASSWORD
        ).send_keys(password)

        driver.find_element(
            *Locators.INPUT_PASSWORD_CONFIRM
        ).send_keys(password)

        driver.find_element(
            *Locators.BTN_CREATE_ACCOUNT
        ).click()

        wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.USER_ELEMENT
            )
        )

        # Выходим из аккаунта
        wait.until(
            expected_conditions.element_to_be_clickable(
                Locators.LOGOUT_BUTTON
            )
        ).click()

        wait.until(
            expected_conditions.invisibility_of_element_located(
                Locators.USER_ELEMENT
            )
        )

        login_button = wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.BTN_ENTER_REG
            )
        )

        assert login_button.is_displayed()
