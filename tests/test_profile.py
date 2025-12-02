import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page import MainPageLocators
from locators.login_page import LoginPageLocators
from locators.profile_page import ProfilePageLocators

BASE_URL = "https://stellarburgers.education-services.ru/"


def login(driver, email, password):
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
    )


def test_profile_navigation_and_constructor(driver):
    driver.get(BASE_URL)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    login(driver, "vitaliy_gulevaty_35_137@yandex.ru", "qwerty1345")

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
    )

    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
    )

    driver.quit()
