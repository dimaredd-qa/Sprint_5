from selenium.webdriver.common.by import By


class Locators:
    #Поле Имя
    field_name = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    # Поле Email
    field_email = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # Поле пароль
    field_password = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    #Кнопка Зарегистрироваться
    button_register = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")

    #Кнопка Войти
    button_entrance = (By.XPATH, "//button[contains(text(), 'Войти')]")

    #Уведомление пользователь существует
    alert_existing_user = (By.XPATH, "//p[contains(text(), 'уже существует')]")

    # Уведомление некорректный пароль
    alert_incorrect_password = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

    #Кнопка "Войти в аккаунт"
    button_login_main_site = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")

    #Кнопка "Оформить заказ"
    button_register_order = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    #Кнопка "Личный кабинет"
    button_personal_account = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

    # Кнопка Войти
    button_entrance_from_registration = (By.XPATH, "//a[contains(text(), 'Войти')]")

    #Кнопка Выйти
    button_exit = (By.XPATH, "//button[contains(text(), 'Выход')]")

    #Заголовок страницы "Лента заказов"
    header_table_order = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")

    #Кнопка "Конструктор"
    button_constructor = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    #Лого "Stella Burgers"
    logo_stella_burgers = (By.XPATH, "//a[contains(@href, '/')]")

    #Раздел "Начинки"
    filling_layer = (By.XPATH, "//span[contains(text(), 'Начинки')]")

    # Раздел "Соусы"
    sauce_layer = (By.XPATH, "//span[contains(text(), 'Соусы')]")

    # Раздел "Булки"
    bread_layer = (By.XPATH, "//span[contains(text(), 'Булки')]")

    #Активный раздел слоев бургера
    action_layer = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    #Надпись соусы
    text_sauce = (By.XPATH, "//span[contains(text(), 'Соусы')]")