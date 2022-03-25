# Author: Marci Devuaughan
# Created: 04 February 2022
# Updated: 04 February 2022
# Maps Team to Trade Number

from sys import argv
import json

fi = open("2022NHLTDL.json", "r")
data = json.load(fi)
fi.close()

for trade in data:
    team1 = trade['team1']
    team2 = trade['team2']
    team3 = False
    print(team1['name'])
    print(team2['name'])
    if team3:
      print(team3['name'])