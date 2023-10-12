from src.infra.web_scrapping.repositories.repository_scrappy import RepositoryScrappy
from src.utils.xpath import Player

class InsertPlayer(RepositoryScrappy):
    def __init__(self) -> None:
        pass
    
    def insert_player(self):
        self.init_web_driver('https://valorantstats.xyz/')
        self.insert_value_element(Player.INPUT_PLAYER, 'sacy')
        self.click_element(Player.PLAYER)