from src.interfaces.scrappy_interface import StatusScrappyInterface
from src.infra.web_scrapping.settings.connection import ConnectionWeb
from src.infra.web_scrapping.settings.element import Element

class RepositoryScrappy(StatusScrappyInterface):

    def init_web_driver(self, url):
        with ConnectionWeb() as connector:
            self.driver = connector.init_web_driver()
            connector.page_navigate(url)
        
    def get_element(self, xpath):
        with Element(self.driver) as finder:
            self.element = finder.find_element(xpath)
            return self.element

    def get_value_element(self, xpath):
        with Element(self.driver) as setter:
            self.element = setter.find_element(xpath)
            return self.element.text

    def insert_value_element(self, xpath, keys):
        with Element(self.driver) as setter:
            self.element = setter.set_value_element(xpath, keys)

    def click_element(self, xpath):
        with Element(self.driver) as clicker:
            self.element = clicker.click_element(xpath)
