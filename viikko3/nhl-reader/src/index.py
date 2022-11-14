import requests
from player import Player


class PlayerReader:
    def __init__(self,url):
        self.url = url
        self.players = []

    def get_players(self):
        response = requests.get(self.url).json()

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['games'],
                player_dict['goals'],
                player_dict['assists']
            )
            self.players.append(player)

        return self.players

class PlayerStats(PlayerReader):
    def __init__(self,reader):
        self.reader = reader.get_players()
        self.players = self.reader
    
    def top_scorers_by_nationality(self,nationality):
        players = [x for x in self.players if x.nationality == nationality]
        players.sort(key=lambda player: player.points, reverse=True)
        return players

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

main()