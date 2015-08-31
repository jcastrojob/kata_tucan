__author__ = 'jcastro'


class Player(object):
    def __init__(self):
        self.nick = None
        self.name = None
        self.team = None
        self.number = None
        self.games = {}

    def add_game(self, game, split):
        if game not in self.games:
            team = split[3]
            position = split[4]
            score = []
            for i in range(5, len(split)):
                score.append(split[i])

            self.games[game] = {'team': team, 'position': position, 'score': score}