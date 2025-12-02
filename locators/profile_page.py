from selenium.webdriver.common.by import By

class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")
