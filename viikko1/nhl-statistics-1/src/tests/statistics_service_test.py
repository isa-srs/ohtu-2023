import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search(self):
        self.assertEqual(self.stats.search('Kurri').name, 'Kurri')
    
    def test_search_none(self):
        self.assertEqual(self.stats.search('Matthews'), None)
    
    def test_team_list(self):
        team_players = self.stats.team('EDM')

        self.assertEqual(team_players[0].name, 'Semenko')
        self.assertEqual(len(team_players), 3)
    
    def test_top_by_points(self):
        top = self.stats.top(0, 1)

        self.assertEqual(top[0].name, 'Gretzky')

    def test_top_by_goals(self):
        top = self.stats.top(0, 2)

        self.assertEqual(top[0].name, 'Lemieux')
    
    def test_top_by_assists(self):
        top = self.stats.top(0, 3)

        self.assertEqual(top[0].name, 'Gretzky')
    
    def test_top_not_sorted(self):
        self.assertEqual(self.stats.top(0,0), None)
        