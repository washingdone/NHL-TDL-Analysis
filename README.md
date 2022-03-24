# NHL-TDL-Analysis
A group of programs to parse NHL Trade Deadline Data

**Warning:** This project is in an unfinished state and should not be expected to function properly. This repo is uploaded for posterity's sake.

## Data Format
Data should be a standard CSV file with the following heading included
```csv
Team 1,Team 2,Team 3,Players 1,Picks 1,Notes 1,Players 2,Picks 2,Notes 2,Players 3,Picks 3,Notes 3
```
The Team columns must contain only one entry, however the rest of the columns may contain more than one entry. If multiple entries are required, they should be seperated with `; `
For further reference please see the [2022NHLTDL](./2022NHLTDL.csv) file

## Workflows
Workflows will be considered as starting from the root of this collection
Commands listed are verified for powershell
### Python
#### Command Arguments
- --keepEmptyData (-k)
  - Maintains rows that would only contain one data value on programs that default to ignore
#### Example Commands
- cat .\2022NHLTDL.csv | python .\python\MapTrades.py | sort | python .\python\CountTeamTrades.py`
  - Counts number of trades per team