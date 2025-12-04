import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.constructor_page import ConstructorPageLocators


class TestConstructor:

    @pytest.mark.parametrize("tab_name, tab_locator", [
        ("Булки", ConstructorPageLocators.TAB_BUNS),
        ("Соусы", ConstructorPageLocators.TAB_SAUCES),
        ("Начинки", ConstructorPageLocators.TAB_TOPPINGS)
    ])
    def test_navigate_tabs(self, open_main_page, tab_name, tab_locator):
        driver = open_main_page

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(tab_locator)
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        ActionChains(driver).move_to_element(element).click().perform()

        active_tab = driver.find_element(*ConstructorPageLocators.ACTIVE_TAB)
        assert tab_name in active_tab.text
