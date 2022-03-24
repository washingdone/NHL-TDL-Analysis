# Author: Marci Devuaughan
# Created: 04 February 2022
# Updated: 04 February 2022
# Counts number of Picks per Team

from re import findall
from sys import stdin
fo = open("TeamPlayers.csv", "w")

currentKey = ""
currentValue = 0

for line in stdin:
  rowData = line.strip().split(',')
  team, players = rowData
  if team != currentKey: # check if current key is equal to key being scanned
    if currentKey: # check that key has been initialized

      # output the last key value pair result
      fo.write(currentKey + ',' + str(currentValue) + '\n')

    # start over when changing keys
    currentKey = team
    currentValue = 0

  # increase count by one
  currentValue += 1

# output the final entry when done
fo.write(currentKey + ',' + str(currentValue) + '\n')
fo.close()