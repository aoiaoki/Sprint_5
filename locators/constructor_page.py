from selenium.webdriver.common.by import By

class ConstructorLocators:
    TAB_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TAB_TOPPINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'current')]")