from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class Statistics:
    def __init__(self,pr):
        self.pr = pr
        self._players = self.pr.get_players()


    def sort_by_points(self,player):
        return player.points

    def sort_by_goals(self,player):
        return player.goals
    
    def sort_by_assists(self,player):
        return player.assists

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

    def top(self,how_many,how_sort):
        how_sort = SortBy(how_sort).value
        
        if how_sort == 1:
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

        elif how_sort == 2:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=self.sort_by_goals
            )
            
            result = []
            i = 0
            while i <= how_many:
                result.append(sorted_players[i])
                i += 1

            return result

        else:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=self.sort_by_assists
            )
        
            result = []
            i = 0
            while i <= how_many:
                result.append(sorted_players[i])
                i += 1

            return result
        
