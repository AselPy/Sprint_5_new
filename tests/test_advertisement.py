
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


def test_open_advertisement(driver):
    wait = WebDriverWait(driver, 15)

    wait.until(
        expected_conditions.element_to_be_clickable(
            Locators.PLACE_AD_BUTTON
        )
    ).click()

    message = wait.until(
        expected_conditions.visibility_of_element_located(
            Locators.AUTHORIZATION_MODAL
        )
    )

    assert message.is_displayed()
