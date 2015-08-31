# kata_tucan
Kata in python 3

Tucan Tournament is a tournament where several players compete in several sports. Right now, the sports played are basketball and handball games. They plan to add more sports in the future.
You have been contacted to create a program to calculate the Most Valuable Player (MVP) of the tournament.

You will receive a set of files, each one containing the stats of one game. Each file will start with a row indicating the sport it refers to.
Each player is assigned a unique nickname.
Each file represent a single game.

The MVP is the player with the most rating points, adding the rating points in all games.

A player will receive 10 additional rating points if their team won the game. Every game must have a winner team. One player may play in different teams and positions in different games, but not in the same game.
The program responsible of generating the files has a bug, that can be reflected in wrong files format. If one file is wrong, the whole set of files is considered to be wrong and the MVP won't be calculated.

# Basketball:
Each row will represent one player stats, with the format:
player name;nickname;number;team name;position;scored points;rebounds;assists
This table details the rating points each player in a basketball game receives depending on her position:

E.g. a player playing as center with 10 scored points, 5 rebounds and no assists will be granted 25 rating points (10*2 + 5*1 + 0*3 ).
The winner team is the one with more scored points. Example:

BASKETBALL
player 1;nick1;4;Team A;G;10;2;7
player 2;nick2;8;Team A;F;0;10;0
player 3;nick3;15;Team A;C;15;10;4
player 4;nick4;16;Team B;G;20;0;0
player 5;nick5;23;Team B;F;4;7;7
player 6;nick6;42;Team B;C;8;10;0