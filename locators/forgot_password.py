from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.NAME, "name")  # поле почты
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    GO_TO_LOGIN = (By.XPATH, "//a[text()='Войти']")  # ссылка на логин
