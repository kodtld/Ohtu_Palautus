import unittest
from statistics import Statistics
from player import Player
from statistics import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
        self.players = PlayerReaderStub.get_players(self)
        self.player = PlayerReaderStub.get_players(self)[0]
        self.fake_player = Player("Petteri", "HJK", 2, 3)
        self.sort_points = SortBy(1)
        print(self.sort_points)

    def test_sort_by_points(self):
        points = self.statistics.sort_by_points(self.player)
        self.assertAlmostEqual(points,16)

    def test_search(self):
        player = self.statistics.search(self.player.name)
        self.assertEqual(player.name,"Semenko")
    
    def test_search_unvalid(self):
        player = self.statistics.search(self.fake_player.name)
        self.assertEqual(player,None)

    def test_team(self):
        player = self.statistics.team("PIT")
        self.assertEqual(player[0].name,"Lemieux")
    
    def test_top_points(self):
        player = self.statistics.top(1,SortBy.POINTS)
        self.assertEqual(player[0].name,"Gretzky")
    
    def test_top_goals(self):
        player = self.statistics.top(1,SortBy.GOALS)
        print(SortBy.GOALS)
        self.assertEqual(player[0].name,"Lemieux")
    
    def test_top_assists(self):
        player = self.statistics.top(1,SortBy.ASSISTS)
        self.assertEqual(player[0].name,"Gretzky")
