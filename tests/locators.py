
from selenium.webdriver.common.by import By


class Locators:
    # Главная страница: вход и регистрация
    BTN_ENTER_REG = (
        By.XPATH,
        "//*[self::button or self::a or @role='button']"
        "[contains(normalize-space(.), 'Вход и регистрация') "
        "or contains(normalize-space(.), 'Войти') "
        "or contains(normalize-space(.), 'Личный кабинет')]"
    )

    # Переключение на регистрацию
    BTN_NO_ACCOUNT = (
        By.XPATH,
        "//*[self::button or self::a or @role='button']"
        "[contains(normalize-space(.), 'Нет аккаунта') "
        "or contains(normalize-space(.), 'Зарегистрироваться') "
        "or contains(normalize-space(.), 'Регистрация')]"
    )

    # Поле электронной почты
    INPUT_EMAIL = (
        By.XPATH,
        "//input["
        "@type='email' "
        "or @name='email' "
        "or @autocomplete='email' "
        "or contains(translate(@placeholder, "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), 'email') "
        "or contains(translate(@placeholder, "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), 'почт') "
        "or contains(translate(@name, "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), 'email')"
        "]"
    )

    # Поля пароля
    INPUT_PASSWORD = (
        By.XPATH,
        "(//input[@type='password'])[1]"
    )

    INPUT_PASSWORD_CONFIRM = (
        By.XPATH,
        "(//input[@type='password'])[2]"
    )

    # Создание аккаунта
    BTN_CREATE_ACCOUNT = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Создать аккаунт') "
        "or contains(normalize-space(.), 'Зарегистрироваться') "
        "or contains(normalize-space(.), 'Регистрация')]"
    )

    BTN_LOGIN = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Войти')]"
    )

    BTN_LOGOUT = (
        By.XPATH,
        "//*[self::button or self::a or @role='button']"
        "[contains(normalize-space(.), 'Выйти')]"
    )

    USER_ELEMENT = BTN_LOGOUT

    # Сообщения об ошибках
    ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(translate(normalize-space(.), "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', "
        "'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыь'), "
        "'ошибка') "
        "or contains(translate(normalize-space(.), "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), 'invalid') "
        "or contains(normalize-space(.), 'уже зарегистрирован') "
        "or contains(normalize-space(.), 'уже существует')]"
    )

    # Объявления
    BTN_ADD_ADVERTISEMENT = (
        By.XPATH,
        "//*[self::button or self::a or @role='button']"
        "[contains(normalize-space(.), 'Разместить объявление')]"
    )

    MODAL_TITLE_UNAUTHORIZED = (
        By.XPATH,
        "//*[contains(normalize-space(.), "
        "'Чтобы разместить объявление, авторизуйтесь')]"
    )

    INPUT_TITLE = (By.NAME, "name")
    INPUT_DESCRIPTION = (By.NAME, "description")
    INPUT_PRICE = (By.NAME, "price")

    BTN_PUBLISH = (
        By.XPATH,
        "//form[@name='new-card']"
        "//button[normalize-space(.)='Опубликовать']"
    )

    ADS_LIST = (By.CLASS_NAME, "places__list")
