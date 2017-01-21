import unittest
from unittest.mock import patch, MagicMock

from pig import game, player, ui
from pig import game
from pig.player import Player



class TestPlay(unittest.TestCase):


    # Test various scenarios ...  but this should give a good idea of whether things are working.

    '''
        1. player rolls a 1 on first roll, turn ends . Score should stay same, not winner

        2. player rolls 2-6 on first roll. does not accumulate enough points to win. elects to end turn. Score should increase, not winner
        3. player rolls 2-6 on first roll. does not accumulate enough points to win. player rolls again 2-6. Player elects to end turn. Score should increase, not winner
        4. player rolls 2-6 on first roll. does not accumulate enough points to win. player rolls again 2-6. Player repeats several times, each time 2-6. Player elects to end turn. Score should increase, not winner
        5. player rolls 2-6 on first roll. does not accumulate enough points to win. player rolls again 1. Score should stay the same, not winner

        6. player rolls 2-6 on first roll and accumulates enough points to win. Score should increase, user is winner
        7. player rolls 2-6 on first roll. does not accumulate enough points to win. player rolls again 2-6, accumulates enough points to win. Score should increase, user is winner

    '''


    def test_play_game_lose(self):

        # 1. player rolls a 1 on first roll, turn ends . Score should stay same, not winner

        test_player = Player('test')

        test_player.score = 10
        test_player.roll_dice = MagicMock(return_value = 1)

        won = test_player.play()
        self.assertIsNone(won)

        self.assertFalse(test_player.winner)
        self.assertEqual(10, test_player.score)


    def test_play_game_roll_pass(self):

        # 2. player rolls 2-6 on first roll. does not accumulate enough points to win. elects to end turn. Score should increase, not winner
        test_player = Player('test')
        test_player.score = 10

        test_player.roll_dice = MagicMock(side_effect = [6])
        test_player.user_roll_again = MagicMock(side_effect = [False])

        won = test_player.play()
        self.assertIsNone(won)

        self.assertFalse(test_player.winner)
        self.assertEqual(16, test_player.score)


    def test_play_game_roll_roll_pass(self):

        #3. player rolls 2-6 on first roll. does not accumulate enough points to win. player rolls again 2-6. Player elects to end turn. Score should increase, not winner

        test_player = Player('test')
        test_player.score = 10
        test_player.roll_dice = MagicMock(side_effect = [4, 3])
        test_player.user_roll_again = MagicMock(side_effect = [True, False])

        won = test_player.play()
        self.assertIsNone(won)

        self.assertFalse(test_player.winner)
        self.assertEqual(17, test_player.score)


    def test_play_game_roll_many(self):

        # 4. player rolls 2-6 on first roll. does not accumulate enough points to win. player rolls again 2-6. Player repeats several times, each time 2-6. Player elects to end turn. Score should increase, not winner

        test_player = Player('test')
        test_player.score = 10
        rolls = [4, 3, 6, 2, 3, 6, 5, 2]
        user_says = [True, True, True, True, True, True, True, False]
        test_player.roll_dice = MagicMock(side_effect = rolls)
        test_player.user_roll_again = MagicMock(side_effect = user_says)

        won = test_player.play()
        self.assertIsNone(won)

        self.assertFalse(test_player.winner)
        self.assertEqual(10 + sum(rolls), test_player.score)


    def test_play_game_roll_lose(self):

        # 5. player rolls 2-6 on first roll. does not accumulate enough points to win. player rolls again 1. Score should stay the same, not winner

        test_player = Player('test')
        test_player.score = 10
        rolls = [4, 1]
        user_says = [True]
        test_player.roll_dice = MagicMock(side_effect = rolls)
        test_player.user_roll_again = MagicMock(side_effect = user_says)

        won = test_player.play()
        self.assertIsNone(won)

        self.assertFalse(test_player.winner)
        self.assertEqual(10, test_player.score)


    def test_play_game_roll_win(self):

        # 6. player rolls 2-6 on first roll and accumulates enough points to win. Score should increase, user is winner

        test_player = Player('test')
        test_player.score = 99

        test_player.roll_dice = MagicMock(return_value = 4)

        won = test_player.play()
        self.assertTrue(won)

        self.assertTrue(test_player.winner)
        self.assertEqual(103, test_player.score)


    def test_play_game_roll_roll_win(self):

        # 7. player rolls 2-6 on first roll. does not accumulate enough points to win. player rolls again 2-6, accumulates enough points to win. Score should increase, user is winner

        test_player = Player('test')
        test_player.score = 91
        rolls = [6, 5]
        user_says = [True]
        test_player.roll_dice = MagicMock(side_effect = rolls)
        test_player.user_roll_again = MagicMock(side_effect = user_says)

        won = test_player.play()
        self.assertTrue(won)

        self.assertTrue(test_player.winner)
        self.assertEqual(102, test_player.score)



    def test_win(self):

        test_player = Player('test')
        test_player.score = 95
        test_player.win(6)  #should win
        self.assertTrue(test_player.winner)
        self.assertEqual(101, test_player.score)

        test_player = Player('test')
        test_player.score = 15
        test_player.win(6)  #should not win
        self.assertFalse(test_player.winner)
        self.assertEqual(15, test_player.score)  #Score should not increase.



    @patch('builtins.input')
    def test_user_roll_again(self, mock_input):

        user_input_data = ['y', 'Y', 'n', 'q', 'pizza', '121221']
        expected_responses = [True, True, False, False, False, False]
        mock_input.side_effect = user_input_data

        test_player = Player('test')

        for expected_response in expected_responses:
            actual_again = test_player.user_roll_again()
            self.assertEqual(expected_response, actual_again)
