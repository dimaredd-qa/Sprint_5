import pytest

from data_project import Credential, Site, RandomEmailPassword
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#Тест регистрации пользователя валидными данными
@pytest.mark.usefixtures('driver')
class TestRegistration:
    def test_valid_registration(self, driver):
        #Регистрация нового пользователя
        driver.get(Site.registration_site)
        #Генерируем тестовые данные
        generator = RandomEmailPassword()
        name, email, password = generator.generate()
        #Заполняем форму регистрации
        driver.find_element(*Locators.field_name).send_keys(name)
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        #Кликаем кнопку регистрации
        driver.find_element(*Locators.button_register).click()
        #Переход на страницу входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_entrance))
        #Вводим данные для формы входа
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        #Кликаем кнопку входа
        driver.find_element(*Locators.button_entrance).click()
        #Проверка успешного входа
        WebDriverWait(driver, 10).until(EC.url_to_be(Site.main_site))
        assert driver.current_url == Site.main_site

#Тесты где одно из полей пустое для регистрации
@pytest.mark.usefixtures('driver')
class TestRegistrationOneFieldNull:
    def test_registration_field_name_null(self, driver):
        driver.get(Site.registration_site)
        # Генерируем тестовые данные
        generator = RandomEmailPassword()
        _, email, password = generator.generate()
        #Ввод учетки без имени
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        #Клик по кнопке Зарегистрироваться
        driver.find_element(*Locators.button_register).click()
        assert driver.current_url == Site.registration_site

    def test_registration_field_email_null(self, driver):
        driver.get(Site.registration_site)
        # Генерируем тестовые данные
        generator = RandomEmailPassword()
        name, _, password = generator.generate()
        #Ввод учетки без email
        driver.find_element(*Locators.field_name).send_keys(name)
        driver.find_element(*Locators.field_password).send_keys(password)
        #Клик по кнопке Зарегистрироваться
        driver.find_element(*Locators.button_register).click()
        assert driver.current_url == Site.registration_site

    def test_registration_field_password_null(self, driver):
        driver.get(Site.registration_site)
        # Генерируем тестовые данные
        generator = RandomEmailPassword()
        name, email, _ = generator.generate()
        #Ввод учетки без password
        driver.find_element(*Locators.field_name).send_keys(name)
        driver.find_element(*Locators.field_email).send_keys(email)
        #Клик по кнопке Зарегистрироваться
        driver.find_element(*Locators.button_register).click()
        assert driver.current_url == Site.registration_site

#Тест email поля без формата
@pytest.mark.usefixtures('driver')
class TestRegistrationEmailFalse:
    def test_registration_field_email_no_symbol_dogs(self, driver):
        driver.get(Site.registration_site)
        # Генерируем тестовые данные
        generator = RandomEmailPassword()
        name, _, password = generator.generate()
        email = 'ser1997yandex.ru'
        # Ввод email без @
        driver.find_element(*Locators.field_name).send_keys(name)
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        # Клик по кнопке Зарегистрироваться
        driver.find_element(*Locators.button_register).click()
        assert driver.current_url == Site.registration_site

#Тест уведомления существующий пользователь
@pytest.mark.usefixtures('driver')
class TestRegistrationExistingUser:
    def test_registration_alert_existing_credential(self, driver):
        driver.get(Site.registration_site)
        # Ввод учетки
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        # Клик по кнопке Зарегистрироваться
        driver.find_element(*Locators.button_register).click()
        #Ожидание Уведомления пользователь существует
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.alert_existing_user))

#Тест уведомления минимального пароля(6 символов)
@pytest.mark.usefixtures('driver')
class TestRegistrationSmallPassword:
    def test_registration_alert_incorrect_password(self, driver):
        driver.get(Site.registration_site)
        # Генерируем тестовые данные
        generator = RandomEmailPassword()
        name, email, _ = generator.generate()
        #Создание и ввод слабого пароля
        password = 123
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_register).click()
        #Ожидание уведомления некорректный пароль
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.alert_incorrect_password))