# Author: Marci Devuaughan
# Created: 04 February 2022
# Updated: 04 February 2022
# Maps Team to Recieved Players

from sys import stdin

stdin.readline()

for line in stdin:
    rowData = line.strip().split(",")
    if len(rowData) == 12:
        team_1,team_2,team_3,players_1,picks_1,notes_1,players_2,picks_2,notes_2,players_3,picks_3,notes_3 = rowData
        print("{0},{1}".format(team_1, players_1))
        print("{0},{1}".format(team_2, players_2))
        if team_3:
          print("{0},{1}".format(team_3, players_3))