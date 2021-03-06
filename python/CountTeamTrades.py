# Author: Marci Devuaughan
# Created: 04 February 2022
# Updated: 04 February 2022
# Counts number of Trades per Team

from re import findall
from sys import stdin
fo = open("TeamTrades.csv", "w")

currentKey = ""
currentValue = 0
i = 0
for line in stdin:
  line = line.strip()
  if line != currentKey: # check if current key is equal to key being scanned
    i = i+ 1
    if currentKey: # check that key has been initialized

      # output the last key value pair result
      fo.write(currentKey + ',' + str(currentValue) + '\n')

    # start over when changing keys
    currentKey = line
    currentValue = 0

  # increase count by one
  currentValue += 1

# output the final entry when done
fo.write(currentKey + ',' + str(currentValue) + '\n')
fo.close()