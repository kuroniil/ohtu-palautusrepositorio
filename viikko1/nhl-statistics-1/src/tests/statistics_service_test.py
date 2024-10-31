import unittest
from statistics_service import StatisticsService, SortBy
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
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_actual_player(self):
        correct_result = Player("Lemieux", "PIT", 45, 54)
        
        tested_result = self.stats.search("Lemieux")

        self.assertEqual(correct_result.name, tested_result.name)
        self.assertEqual(correct_result.team, tested_result.team)
        self.assertEqual(correct_result.goals, tested_result.goals)
        self.assertEqual(correct_result.assists, tested_result.assists)

    def test_search_works_with_nonexistent_player(self):
        tested_result = self.stats.search("Selanne")

        self.assertEqual(tested_result, None)

    def test_team_returns_correct_players(self):
        correct_result = [Player("Semenko", "EDM", 4, 12), Player("Kurri", "EDM", 37, 53), Player("Gretzky", "EDM", 35, 89)]
        correct_result = sorted(list(map(lambda player: player.name, correct_result)))

        tested_result = self.stats.team("EDM")
        tested_result = sorted(list(map(lambda player: player.name, tested_result)))

        self.assertEqual(tested_result, correct_result)

    def test_top_function_works_with_points(self):
        players = PlayerReaderStub().get_players()
        correct_order = list(map(lambda player: (player.name, player.goals + player.assists), players))
        correct_order = sorted(correct_order, key=lambda x: x[1], reverse=True)

        tested_result = self.stats.top(4)
        tested_result = list(map(lambda player: (player.name, player.goals + player.assists), tested_result))

        self.assertEqual(tested_result, correct_order)


    def test_top_function_works_with_goals(self):
        players = PlayerReaderStub().get_players()
        correct_order = list(map(lambda player: (player.name, player.goals), players))
        correct_order = sorted(correct_order, key=lambda x: x[1], reverse=True)

        tested_result = self.stats.top(4, SortBy.GOALS)
        tested_result = list(map(lambda player: (player.name, player.goals), tested_result))

        self.assertEqual(tested_result, correct_order)

    def test_top_function_works_with_assists(self):
        players = PlayerReaderStub().get_players()
        correct_order = list(map(lambda player: (player.name, player.assists), players))
        correct_order = sorted(correct_order, key=lambda x: x[1], reverse=True)

        tested_result = self.stats.top(4, SortBy.ASSISTS)
        tested_result = list(map(lambda player: (player.name, player.assists), tested_result))

        self.assertEqual(tested_result, correct_order)