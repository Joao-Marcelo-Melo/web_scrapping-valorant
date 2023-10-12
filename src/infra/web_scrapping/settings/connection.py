from src.infra.web_scrapping.settings.selenium import *

class ConnectionWeb:
    def __init__(self) -> None:
        self.driver = webdriver.Edge()

    def init_web_driver(self):
        return self.driver
    
    def page_navigate(self, url):
        self.driver.get(url)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
