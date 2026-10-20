from selenium.webdriver.common.by import By


class Locators:
    # Кнопки на главной странице
    LOGIN_REGISTER_BUTTON = (
        By.XPATH, "//*[contains(text(), 'Вход и регистрация')]"
    )

    NO_ACCOUNT_BUTTON = (
        By.XPATH, "//*[contains(text(), 'Нет аккаунта')]"
    )

    LOGOUT_BUTTON = (
        By.XPATH, "//*[contains(text(), 'Выйти')]"
    )

    PLACE_AD_BUTTON = (
        By.XPATH, "//*[contains(text(), 'Разместить объявление')]"
    )

    # Поля регистрации и входа
    INPUT_EMAIL = (
        By.XPATH, "//input[@type='email']"
    )

    INPUT_PASSWORD = (
        By.XPATH, "(//input[@type='password'])[1]"
    )

    INPUT_PASSWORD_CONFIRM = (
        By.XPATH, "(//input[@type='password'])[2]"
    )

    # Кнопки форм
    BTN_CREATE_ACCOUNT = (
        By.XPATH, "//button[contains(text(), 'Создать аккаунт')]"
    )

    BTN_LOGIN = (
        By.XPATH, "//button[contains(text(), 'Войти')]"
    )

    # Сообщение об ошибке
    ERROR_MESSAGE = (
        By.XPATH, "//*[contains(text(), 'Ошибка')]"
    )

    # Элемент с именем пользователя
    USER_ELEMENT = (
        By.XPATH, "//*[contains(text(), 'User')]"
    )

    # Совместимые имена для тестов
    BTN_ENTER_REG = LOGIN_REGISTER_BUTTON
    BTN_NO_ACCOUNT = NO_ACCOUNT_BUTTON
    BTN_LOGOUT = LOGOUT_BUTTON