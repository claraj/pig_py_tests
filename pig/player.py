import pig
from pig import dice
from pig.dice import Dice


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.winner = False


    def roll_dice(self):

        dice = Dice()
        roll = dice.roll()
        print('You rolled a {}'.format(roll))
        return roll


    def win(self, score_this_round):

        if score_this_round + self.score >= 100:
            self.score = self.score + score_this_round
            print('100 or more! You win!')
            self.winner = True
            return True


    def user_roll_again(self):
        again = input('Roll again? Y to roll again, anything else to end your turn:  ')
        return again.lower() == 'y'


    def play(self):

        print('\nPlayer {}, it\'s your turn. Your score is {}'.format(self.name, self.score))

        roll_again = True

        score_this_round = 0

        while roll_again:

            roll = self.roll_dice()

            if roll == 1:    # End turn, nothing added to score
                print('Rolling a 1 ends your turn. Next player\'s turn.')
                return

            score_this_round += roll

            # automatically win if score + score_this_round >= 100

            if self.win(score_this_round):
                return True


            print('''You rolled a {} for a total score this round of {}.
Your score for the game is {} (excluding points for this round), or {} (including points for this round)
'''.format(roll, score_this_round, self.score, self.score+score_this_round))


            if not self.user_roll_again():
                 self.score += score_this_round
                 print('Thanks player {}, that\'s the end of your turn. Your score is {}'.format(self.name, self.score))
                 break
