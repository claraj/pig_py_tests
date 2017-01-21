import unittest
from unittest.mock import patch, MagicMock

from pig import game, player, ui
from pig import game
from pig.player import Player



class TestPig(unittest.TestCase):


    @patch('pig.ui.positive_int_input', return_value=4)
    @patch('pig.ui.get_unique_names', return_value=['a', 'b', 'c', 'd'])
    def test_create_players(self, mock_names, mock_int_input):

        players = game.create_players()

        expectedPlayers = [ Player('a'), Player('b'), Player('c'), Player('d')]

        # Assert the correct number of players is created
        self.assertEqual(len(players), len(expectedPlayers))

        # And that they have the correct names 
        for actual, expected in zip (players, expectedPlayers):
            self.assertEqual(actual.name, expected.name)



    def test_play_game(self):

        #Create some players with a mock Play method
        player_1 = Player('test1')
        player_1.play = MagicMock(side_effect=['', '', '', True])

        player_2 = Player('test2')
        player_2.play = MagicMock(side_effect=['', '', '', ''])

        player_3 = Player('test3')
        player_3.play = MagicMock(side_effect=['', '', '', ''])

        # Test that play continues until a player returns True

        game.play([player_1, player_2, player_3])

        # No need to unpatch because these player objects won't be used after this test.


    @patch('builtins.print')
    def test_display_winners(self, mock_print):

        player_1 = Player('test1')
        player_1.score = 10

        player_2 = Player('test2')
        player_2.winner = True
        player_2.score = 101

        player_3 = Player('test3')
        player_3.score = 20

        # Verify mock_print is called with a message saying player 2 won

        game.results([player_1, player_2, player_3])

        call_args = mock_print.call_args_list

        mock_print.assert_any_call('**** Player name: test2 score: 101 **** is the winner!! *****')
        mock_print.assert_any_call('Player name: test1 score: 10')
        mock_print.assert_any_call('Player name: test3 score: 20')
