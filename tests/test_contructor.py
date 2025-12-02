from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

BASE_URL = "https://stellarburgers.education-services.ru/"


class ConstructorLocators:
    TAB_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TAB_TOPPINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")


@pytest.mark.parametrize("tab_name,tab_locator", [
    ("Булки", ConstructorLocators.TAB_BUNS),
    ("Соусы", ConstructorLocators.TAB_SAUCES),
    ("Начинки", ConstructorLocators.TAB_TOPPINGS)
])
def test_navigate_tabs(driver, tab_name, tab_locator):
    driver.get(BASE_URL)

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(tab_locator)
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

    ActionChains(driver).move_to_element(element).click().perform()

    # Проверка, что вкладка стала активной
    active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")
    assert tab_name in active_tab.text
