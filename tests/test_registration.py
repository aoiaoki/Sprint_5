import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page import MainPageLocators
from locators.login_page import LoginPageLocators
from locators.register_page import RegisterPageLocators
from generator import generate_email, generate_password

BASE_URL = "https://stellarburgers.education-services.ru/"


def test_successful_registration(driver):
    driver.get(BASE_URL)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

    email = generate_email()
    password = generate_password()
    name = "Vitaliy"

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )


def test_registration_with_short_password(driver):
    driver.get(BASE_URL)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

    email = generate_email()
    short_password = "123"
    name = "Vitaliy"

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(short_password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
    )
    assert error_element.text.strip() == "Некорректный пароль"
