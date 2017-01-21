import pig

from pig import ui, player
from pig.player import Player


# from pig import dice, player, ui
#
# from dice import Dice
# from player import Player


'''
Each turn, a player repeatedly rolls a die until either a 1 is rolled or the
player decides to "hold":
If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the
player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it
becomes the next player's turn.
The first player to score 100 or more points wins.
For example, the first player, Ann, begins a turn with a roll of 5. Ann could
hold and score 5 points, but chooses to roll again. Ann rolls a 2, and could
hold with a turn total of 7 points, but chooses to roll again. Ann rolls a 1,
and must end her turn without scoring. The next player, Bob, rolls the
sequence 4-5-3-5-5, after which he chooses to hold, and adds his turn total of
22 points to his score.

-- Rules from Wikipedia; https://en.wikipedia.org/wiki/Pig_(dice_game)
'''

def results(players):

    for player in players:

        if player.winner:
            print('**** Player name: {} score: {} **** is the winner!! *****'.format(player.name, player.score))
        else:
            print('Player name: {} score: {}'.format(player.name, player.score))



def create_players():

    players = []
    number_of_players = ui.positive_int_input('How many players?', 2)
    names = ui.get_unique_names(number_of_players, 'Player')

    players = [ Player(name) for name in names ]    # List comprehensions are also my favorite thing about Python :)
    return players


def play(players):

    while True:
        for player in players:
            is_winner = player.play()
            if is_winner:
                return

def main():

    players = create_players()
    play(players)
    results(players)




if __name__ == '__main__':
    main()
