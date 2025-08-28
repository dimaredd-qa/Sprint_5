import pytest

from selenium import webdriver
from data_project import Credential, Site
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def driver_existing_credential(driver):
    driver.get(Site.login_site)
    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    #Клик по кнопке Вход
    driver.find_element(*Locators.button_entrance).click()
    #Ждем отображение кнопки "Оформить заказ"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_register_order))
    return driver

