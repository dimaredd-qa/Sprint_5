import pytest

from data_project import Credential, Site
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Тест вход через кнопку Войти в аккаунт на главной
@pytest.mark.usefixtures('driver')
class TestButtonEntranceAccountMainSite:
    def test_button_entrance_main_site(self, driver):
        driver.get(Site.main_site)

        # клик кнопки "Войти в аккаунт"
        driver.find_element(*Locators.button_login_main_site).click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_entrance))

        # ввод данных существующего пользователя
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)

        # клик кнопки "Войти"
        driver.find_element(*Locators.button_entrance).click()

        # проверка перехода на главную страницу
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_register_order))


#Тест вход через кнопку Личный кабинет
@pytest.mark.usefixtures('driver')
class TestButtonPersonalAccount:
    def test_button_entrance_personal_account(self, driver):
        driver.get(Site.main_site)

        #клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.button_personal_account).click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_entrance))

        # ввод данных существующего пользователя
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)

        # клик кнопки "Войти"
        driver.find_element(*Locators.button_entrance).click()

        # проверка перехода на главную страницу
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_register_order))


#Тест вход через кнопку в форме регистрации
@pytest.mark.usefixtures('driver')
class TestButtonEntranceFromRegistration:
    def test_button_entrance_main_site(self, driver):
        driver.get(Site.registration_site)

        #клик по кнопке Войти
        driver.find_element(*Locators.button_entrance_from_registration).click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_entrance))

        # ввод данных существующего пользователя
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)

        # клик кнопки "Войти"
        driver.find_element(*Locators.button_entrance).click()

        # проверка перехода на главную страницу
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_register_order))


#Тест вход через кнопку в форме восстановления пароля
@pytest.mark.usefixtures('driver')
class TestButtonEntranceRecoveryPassword:
    def test_button_entrance_recovery_password(self, driver):
        driver.get(Site.password_recovery_site)

        # клик по кнопке Войти
        driver.find_element(*Locators.button_entrance_from_registration).click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_entrance))

        # ввод данных существующего пользователя
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)

        # клик кнопки "Войти"
        driver.find_element(*Locators.button_entrance).click()

        # проверка перехода на главную страницу
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_register_order))

#Тест выхода из аккаунта по кнопке Выйти в личном кабинете
@pytest.mark.usefixtures('driver_existing_credential')
class TestButtonExitAccount:
    def test_button_exit(self, driver_existing_credential):

        #клик по кнопке "Личный кабинет"
        driver_existing_credential.find_element(*Locators. button_personal_account).click()

        #ждем загрузки страницы профиля
        WebDriverWait(driver_existing_credential, 3).until(EC.url_to_be(Site.profile_site))

        # клик по кнопке Выход
        driver_existing_credential.find_element(*Locators.button_exit).click()

        # проверка перехода на страницу Входа
        assert WebDriverWait(driver_existing_credential, 3).until(EC.url_to_be(Site.login_site))

