import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.credentials import BASE_URL, EMAIL, PASSWORD
from locators.main_page import MainPageLocators
from locators.login_page import LoginPageLocators
from locators.profile_page import ProfilePageLocators



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(driver):
    driver.get(BASE_URL)
    return driver


@pytest.fixture
def login_user(driver):
    def _login(email=EMAIL, password=PASSWORD):

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

        return driver

    return _login

