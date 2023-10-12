from src.infra.web_scrapping.settings.selenium import *
import pyautogui

class Element:
    def __init__(self, driver) -> None:
        self.driver = driver

    def find_element(self, xpath):
        self.element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def set_value_element(self, xpath, keys):
        self.find_element(xpath)
        self.element.send_keys(keys)
        self.element.submit()

    def click_element(self, xpath):
        self.find_element(xpath)
        self.element.click()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
