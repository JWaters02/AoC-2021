# AoC-2021

Repository for my solutions to Advent of Code 2021. 

I calculated the overall execution time from each part 1 and part 2 solutions (given my own inputs) alongside my time completion of puzzles (from 5am UTC start time) and my global rank for them:

Day | Part 1 Time | Part 2 Time (Accumulated) | Overall Execution Time (s) | Global Rank
--- | ----------- | ------------------------- | -------------------------- | -----------
[Day 1](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day1.py) | 00:13:37 | 00:27:13 | 0.003 | 5960
[Day 2](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day2.py) | 00:16:35 | 00:19:02 | 0.002 | 7843
[Day 3](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day3.py) | 00:28:22 | 00:42:05 | 0.003 | 4294
[Day 4](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day4.py) | 01:05:35 | 01:19:33 | 0.05 | 5906
[Day 5](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day5.py) | 00:25:35 | 00:38:44 | 0.13 | 2995
Day 6 |  |  |  | 
Day 7 |  |  |  | 
Day 8 |  |  |  | 
Day 9 |  |  |  | 
Day 10 |  |  |  | 
Day 11 |  |  |  | 
Day 12 |  |  |  | 
Day 13 |  |  |  | 
Day 14 |  |  |  | 
Day 15 |  |  |  | 
Day 16 |  |  |  | 
Day 17 |  |  |  | 
Day 18 |  |  |  | 
Day 19 |  |  |  | 
Day 20 |  |  |  | 
Day 21 |  |  |  | 
Day 22 |  |  |  | 
Day 23 |  |  |  | 
Day 24 |  |  |  | 
Day 25 |  |  |  |  

## Blueprint Solutions
### Day 1
![Day 1](https://github.com/JWaters02/AoC-2021/blob/1fe0359ac5857d86f953a2cc7ce757c69566648c/BP%20Solutions/Day1.png)
### Day 2
![Day 2](https://github.com/JWaters02/AoC-2021/blob/75870dbf4b672cee0828152249e79db9554186a9/BP%20Solutions/Day2.png)
### Day 3
There were a few different functions for various processes so I took screenshots of the most important ones. The first screenshot is the main function for parts 1 and 2. I wrote the BP code based off my Python solution.
![Day 3 Main](https://github.com/JWaters02/AoC-2021/blob/fca008441a60551cfa25132d53895f3fe55dbb9c/BP%20Solutions/Day3-Main.png)
![Day 3 Create Counter](https://github.com/JWaters02/AoC-2021/blob/fca008441a60551cfa25132d53895f3fe55dbb9c/BP%20Solutions/Day3-CreateCounter.png)
![Day 3 Binary To Decimal](https://github.com/JWaters02/AoC-2021/blob/fca008441a60551cfa25132d53895f3fe55dbb9c/BP%20Solutions/Day3-BinToDec.png)
![Day 3 Get Rating](https://github.com/JWaters02/AoC-2021/blob/fca008441a60551cfa25132d53895f3fe55dbb9c/BP%20Solutions/Day3-GetRating.png)
The above function is effectively the main function for part 2, but since it gets called twice for the oxygen and C02 scrubbers I had to make it a separate function.
![Day 3 Filter Lines](https://github.com/JWaters02/AoC-2021/blob/fca008441a60551cfa25132d53895f3fe55dbb9c/BP%20Solutions/Day3-FilterLines.png)
### Day 4
Day 4's input is so complex that I just did not want to spend the time to write a solution in BP.