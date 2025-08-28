import pytest

from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Тест переход к разделам "Начинки"
@pytest.mark.usefixtures('driver_existing_credential')
class TestTransitionFilling:
    def test_transition_filling(self, driver_existing_credential):
        # жмав раздел "Начинки"
        driver_existing_credential.find_element(*Locators.filling_layer).click()
        # Проверка активного раздела Начинки на наличие фиолетовой полоски
        action = WebDriverWait(
            driver_existing_credential, 3
        ).until(EC.visibility_of_element_located(Locators.action_layer))
        assert "Начинки" in action.text


# Тест переход к разделам "Соусы"
@pytest.mark.usefixtures('driver_existing_credential')
class TestTransitionSauce:
    def test_transition_sauce(self, driver_existing_credential):
        # жмав раздел "Соусы"
        driver_existing_credential.find_element(*Locators.sauce_layer).click()
        # Проверка активного раздела Начинки на наличие фиолетовой полоски
        action = WebDriverWait(
            driver_existing_credential, 3
        ).until(EC.visibility_of_element_located(Locators.action_layer))
        assert "Соусы" in action.text


# Тест переход к разделам "Булки"
@pytest.mark.usefixtures('driver_existing_credential')
class TestTransitionBread:
    def test_transition_bread(self, driver_existing_credential):
        # жмав раздел "Соусы"
        driver_existing_credential.find_element(*Locators.sauce_layer).click()
        WebDriverWait(driver_existing_credential, 3).until(
            EC.visibility_of_element_located(Locators.text_sauce)
        )
        driver_existing_credential.find_element(*Locators.bread_layer).click()
        # Проверка активного раздела Начинки на наличие фиолетовой полоски
        action = WebDriverWait(
            driver_existing_credential, 3
        ).until(EC.visibility_of_element_located(Locators.action_layer))
        assert "Булки" in action.text