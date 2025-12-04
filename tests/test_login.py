import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page import MainPageLocators
from locators.login_page import LoginPageLocators
from locators.profile_page import ProfilePageLocators
from locators.register_page import RegisterPageLocators
from locators.forgot_password import ForgotPasswordPageLocators
from data.credentials import BASE_URL, EMAIL, PASSWORD


class TestLogin:

    def test_login_from_main_page_button(self, open_main_page, login_user):
        driver = open_main_page
        # Клик по кнопке "Войти" на главной странице
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Логин
        login_user(EMAIL, PASSWORD)

        # Проверка: видна кнопка выхода — значит авторизация успешна
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

    def test_login_from_personal_account_button(self, open_main_page, login_user):
        driver = open_main_page
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        login_user(EMAIL, PASSWORD)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

    def test_login_from_register_flow(self, open_main_page, login_user):
        driver = open_main_page
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

        # Перейти обратно на форму логина (в потоке регистрации есть ссылка)
        driver.find_element(*RegisterPageLocators.GO_TO_LOGIN).click()

        login_user(EMAIL, PASSWORD)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

    def test_login_from_forgot_password_flow(self, open_main_page, login_user):
        driver = open_main_page
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.RESTORE_PASSWORD_LINK).click()

        driver.find_element(*ForgotPasswordPageLocators.GO_TO_LOGIN).click()

        login_user(EMAIL, PASSWORD)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )
