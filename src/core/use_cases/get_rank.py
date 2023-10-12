from src.infra.web_scrapping.repositories.repository_scrappy import RepositoryScrappy
from src.core.entities.players import Player
from src.utils.player_url import players_url


class GetRank(RepositoryScrappy):

    def get_rank(self):
        self.scrappy_rank()