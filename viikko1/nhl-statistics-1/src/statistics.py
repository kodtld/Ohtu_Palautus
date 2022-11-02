class Statistics:
    def __init__(self,pr):
        self.pr = pr

        self._players = self.pr.get_players()


    def sort_by_points(self,player):
        return player.points

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=self.sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
