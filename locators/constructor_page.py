from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    TAB_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TAB_TOPPINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")
    PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
