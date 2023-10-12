from typing import List

class Player:
    def __init__(self, player_name) -> None:
        self.player_url = player_name

    def return_players(self):
        return self.player_url
