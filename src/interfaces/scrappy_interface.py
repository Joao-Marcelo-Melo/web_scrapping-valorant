from abc import ABC, abstractmethod

class StatusScrappyInterface(ABC):

    @abstractmethod
    def init_web_driver():
        pass

    @abstractmethod
    def get_element():
        pass

    @abstractmethod
    def get_value_element():
        pass

    @abstractmethod
    def insert_value_element(self):
        pass
