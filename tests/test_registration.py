
from uuid import uuid4

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestRegistration:

    def open_registration(self, driver):
        wait = WebDriverWait(driver, 15)

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

        email_field = wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.INPUT_EMAIL
            )
        )

        return wait, email_field

    def fill_registration_form(self, driver, email, password):
        driver.find_element(
            *Locators.INPUT_PASSWORD
        ).send_keys(password)

        driver.find_element(
            *Locators.INPUT_PASSWORD_CONFIRM
        ).send_keys(password)

    def test_successful_registration(self, driver):
        wait, email_field = self.open_registration(driver)

        email = f"user_{uuid4().hex[:12]}@example.com"
        password = "TestPassword123!"

        email_field.send_keys(email)
        self.fill_registration_form(driver, email, password)

        driver.find_element(
            *Locators.BTN_CREATE_ACCOUNT
        ).click()

        user = wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.USER_ELEMENT
            )
        )

        avatar = wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.AVATAR
            )
        )

        assert user.is_displayed() and avatar.is_displayed()

    def test_registration_invalid_email_format(self, driver):
        wait, email_field = self.open_registration(driver)

        email_field.send_keys("incorrect_email_format")
        self.fill_registration_form(
            driver, "incorrect_email_format", "TestPassword123!"
        )

        driver.find_element(
            *Locators.BTN_CREATE_ACCOUNT
        ).click()

        error = wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.ERROR_MESSAGE
            )
        )

        email_error = driver.find_element(
            *Locators.EMAIL_ERROR_FIELD
        )

        password_error = driver.find_element(
            *Locators.PASSWORD_ERROR_FIELD
        )

        confirm_error = driver.find_element(
            *Locators.PASSWORD_CONFIRM_ERROR_FIELD
        )

        assert (
            error.is_displayed()
            and email_error.is_displayed()
            and password_error.is_displayed()
            and confirm_error.is_displayed()
        )

    def test_registration_existing_user(self, driver):
        wait, email_field = self.open_registration(driver)

        email = f"existing_{uuid4().hex[:12]}@example.com"
        password = "TestPassword123!"

        email_field.send_keys(email)
        self.fill_registration_form(driver, email, password)

        driver.find_element(
            *Locators.BTN_CREATE_ACCOUNT
        ).click()

        wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.USER_ELEMENT
            )
        )

        wait.until(
            expected_conditions.element_to_be_clickable(
                Locators.LOGOUT_BUTTON
            )
        ).click()

        wait, email_field = self.open_registration(driver)

        email_field.send_keys(email)
        self.fill_registration_form(driver, email, password)

        driver.find_element(
            *Locators.BTN_CREATE_ACCOUNT
        ).click()

        error = wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.ERROR_MESSAGE
            )
        )

        email_error = driver.find_element(
            *Locators.EMAIL_ERROR_FIELD
        )

        password_error = driver.find_element(
            *Locators.PASSWORD_ERROR_FIELD
        )

        confirm_error = driver.find_element(
            *Locators.PASSWORD_CONFIRM_ERROR_FIELD
        )

        assert (
            error.is_displayed()
            and email_error.is_displayed()
            and password_error.is_displayed()
            and confirm_error.is_displayed()
        )
