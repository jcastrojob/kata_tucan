__author__ = 'jcastro'

from player import Player


class Tournament(object):
    players = {}
    games = {}

    @classmethod
    def parser(cls, game, string):
        split = string.split(';')
        player = cls.find_player(split)
        player.add_game(game, split)

    @classmethod
    def find_player(cls, split):
        nick = split[1]
        if nick not in cls.players:
            player = Player()
            player.nick = split[1]
            player.name = split[0]
            player.number = split[2]
            player.team = split[3]
            cls.players[player.nick] = player

        return cls.players[nick]

    def show_players(self):
        return self.players.keys()

    def show_game(self, nick):
        if nick in self.players:
            games = self.games.keys()
        else:
            games = ""

        return games

    def create_game(self, name_game, game_class):
        if name_game not in self.games:
            self.games[name_game] = game_class

    def mvp(self):
        player_score = {}
        for game_name in self.games.keys():
            team_score = {}
            team_members = {}

            for player_nick in self.players.keys():
                player = self.players[player_nick]
                if game_name in player.games:
                    player_game = player.games[game_name]
                    game = self.games[game_name]
                    total_score_player = game.calculate_score(player_game)

                    #save player score
                    if player.nick in player_score:
                        player_score[player.nick] += total_score_player
                    else:
                        player_score[player.nick] = total_score_player

                    #save team score if team win all members win 10 points extra
                    name_team = player.team
                    if name_team in team_score:
                        team_score[name_team] += total_score_player
                    else:
                        team_score[name_team] = total_score_player

                    #save member team
                    if name_team in team_members:
                        members = team_members[name_team]
                        members.append(player.nick)
                    else:
                        team_members[name_team] = [player_nick]

            #find team winer and all player for this team win 10 points extra
            name_team_winer = max(team_score, key=lambda k: team_score[k])
            player_team_winer = team_members[name_team_winer]
            for player_nick in player_team_winer:
                player_score[player_nick] += 10

        print(player_score)

        player_nick_winer = max(player_score, key=lambda k: player_score[k])
        return player_nick_winer




