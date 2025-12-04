import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators.main_page import MainPageLocators
from locators.profile_page import ProfilePageLocators
from locators.login_page import LoginPageLocators
from data.credentials import BASE_URL


class TestProfile:

    def test_profile_navigation_and_constructor(self, open_main_page, login_user):
        driver = open_main_page

        # Клик по "Личный кабинет" и логин через фикстуру
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        login_user()  # использует данные из data/credentials.py

        # Убедиться что кнопка logout видна
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

        # Перейти в конструктор и проверить заголовок
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
        )
