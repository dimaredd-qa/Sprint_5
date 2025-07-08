import pytest

from data_project import Credential, Site
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#Тест переход в личный кабинет из ленты заказов
@pytest.mark.usefixtures('driver_existing_credential')
class TestTransitionAccount:
    def test_transition_acc(self, driver_existing_credential):
        driver_existing_credential.get(Site.table_order)
        WebDriverWait(driver_existing_credential, 5).until(EC.visibility_of_element_located(Locators.header_table_order))
        # клик по кнопке "Личный кабинет"
        driver_existing_credential.find_element(*Locators.button_personal_account).click()
        # ждем загрузки страницы профиля
        WebDriverWait(driver_existing_credential, 3).until(EC.url_to_be(Site.profile_site))
        assert driver_existing_credential.current_url == Site.profile_site

#Тест переход по клику "Конструктор"
@pytest.mark.usefixtures('driver_existing_credential')
class TestTransitionConstructor:
    def test_transition_constructor(self, driver_existing_credential):
        #Клик по кнопке "Конструктор"
        driver_existing_credential.find_element(*Locators.button_constructor)
        assert driver_existing_credential.current_url == Site.main_site

#Тест переход по клику логотипа "Stella Burgers"
@pytest.mark.usefixtures('driver_existing_credential')
class TestTransitionLogo:
    def test_transition_logo(self, driver_existing_credential):
        #Клик по Лого
        driver_existing_credential.find_element(*Locators.logo_stella_burgers)
        assert driver_existing_credential.current_url == Site.main_site