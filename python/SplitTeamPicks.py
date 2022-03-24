# Author: Marci Devuaughan
# Created: 04 February 2022
# Updated: 04 February 2022
# Splits out picks recieved

from sys import stdin,argv

keepPicks = False
if len(argv) > 1:
  keepPicks = (argv[1].find("-k") > -1)

stdin.readline()

for line in stdin:
    rowData = line.strip().split(",")
    if len(rowData) == 2:
        team, picks = rowData
        if picks or keepPicks:
          for pick in picks.split("; "):
            print("{0},{1}".format(team, pick))