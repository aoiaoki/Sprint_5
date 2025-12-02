import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page import MainPageLocators
from locators.login_page import LoginPageLocators
from locators.profile_page import ProfilePageLocators
from locators.register_page import RegisterPageLocators
from locators.forgot_password import ForgotPasswordPageLocators

BASE_URL = "https://stellarburgers.education-services.ru/"
EMAIL = "vitaliy_gulevaty_35_137@yandex.ru"
PASSWORD = "qwerty1345"


def login(driver, email, password):
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()


def open_profile(driver):
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()


def assert_logged_in(driver):
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
    )


def test_login_from_main_page_button(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    login(driver, EMAIL, PASSWORD)
    open_profile(driver)
    assert_logged_in(driver)


def test_login_from_personal_account_button(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    login(driver, EMAIL, PASSWORD)
    open_profile(driver)
    assert_logged_in(driver)


def test_login_from_register_form(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

    driver.find_element(*RegisterPageLocators.GO_TO_LOGIN).click()

    login(driver, EMAIL, PASSWORD)
    open_profile(driver)
    assert_logged_in(driver)


def test_login_from_forgot_password(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LoginPageLocators.RESTORE_PASSWORD_LINK).click()

    driver.find_element(*ForgotPasswordPageLocators.GO_TO_LOGIN).click()

    login(driver, EMAIL, PASSWORD)
    open_profile(driver)
    assert_logged_in(driver)
