__author__ = 'jcastro'

from tournament import Tournament

import abc


class Game(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calculate_score(self, score):
        """Returns final score for player"""


class Basketball(Game):

    point_position = {
        'G': [2, 3, 1],
        'F': [2, 2, 2],
        'C': [2, 1, 3]
    }

    def calculate_score(self, game):
        score_player = game['score']
        position_player = game['position']
        score_total = 0
        if position_player in self.point_position:
            score_position = self.point_position[position_player]

            for i in range(len(score_player)):
                score_total += int(score_player[i]) * int(score_position[i])

        return score_total

# player 1;nick1;4;Team A;G;10;2;7
# player 2;nick2;8;Team A;F;0;10;0
# player 3;nick3;15;Team A;C;15;10;4
# player 4;nick4;16;Team B;G;20;0;0
# player 5;nick5;23;Team B;F;4;7;7
# player 6;nick6;42;Team B;C;8;10;0

my_tournament = Tournament()

my_tournament.create_game("basketball", Basketball())
strPlayer = "player 1;nick1;4;Team A;G;10;2;7"
strPlayer2 = "player 2;nick2;8;Team A;F;0;10;0"
strPlayer3 = "player 4;nick4;16;Team B;G;20;0;0"
my_tournament.parser("basketball", strPlayer)
my_tournament.parser("basketball", strPlayer2)
my_tournament.parser("basketball", strPlayer3)

my_tournament.create_game("basketballHARD", Basketball())
strPlayer = "player 1;nick1;4;Team A;G;10;2;7"
strPlayer2 = "player 2;nick2;8;Team A;F;0;10;0"
strPlayer3 = "player 4;nick4;16;Team B;G;230;0;0"
my_tournament.parser("basketballHARD", strPlayer)
my_tournament.parser("basketballHARD", strPlayer2)
my_tournament.parser("basketballHARD", strPlayer3)

print(my_tournament.mvp())