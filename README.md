# AoC-2021

Repository for my solutions to Advent of Code 2021. 

I calculated the overall execution time from each part 1 and part 2 solutions (given my own inputs) alongside my time completion of puzzles (from 5am UTC start time) and my global rank for them:

Day | Part 1 Time | Part 2 Time (Accumulated) | Overall Execution Time (s) | Global Rank
--- | ----------- | ------------------------- | -------------------------- | -----------
[Day 1](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day1.py) | 00:13:37 | 00:27:13 | 0.002 | 5960
[Day 2](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day2.py) | 00:16:35 | 00:19:02 | 0.002 | 7843
[Day 3](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day3.py) | 00:28:22 | 00:42:05 | 0.001 | 4294
[Day 4](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day4.py) | 01:05:35 | 01:19:33 | 0.050 | 5906
[Day 5](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day5.py) | 00:25:35 | 00:38:44 | 0.130 | 2995
[Day 6](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day6.py) | 00:15:52 | 00:24:23 | 0.503 | 2685
[Day 7](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day7.py) | 00:10:59 | 00:19:08 | 0.400 | 4856
[Day 8](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day8.py) | 00:53:40[^1] | 01:35:09 | 0.005 | 4498
[Day 9](https://github.com/JWaters02/AoC-2021/blob/main/Python/Day9.py) | 00:37:06 | 01:37:18 | 0.005 | 7399
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

[^1]: I woke up 35 minutes late.

## Blueprint Solutions
My goal with these blueprint solutions is that I want to try and match them to the Python solutions I write first. If I find a better way of doing things, I update it in the Python solution first, and then update the blueprint solution. This is partially because I find it difficult to write BP if I don't have code to follow along with. Building upon this, it makes debugging the BP solution much easier since I can debug the Python solution as a reference. The only times this does not hold directly true is when I use a datastructure or library that does not exist in BP and I have to recreate with something my own, for example a defaultdict or Counter from collections. 
### Reading in the input
BP cannot do file I/O on its own so I had to write a couple of small C++ functions to read in the input.
![Read Input C++](https://github.com/JWaters02/AoC-2021/blob/71b4748523fedc471236bfe92ee61b2a52047428/BP%20Solutions/ReadInput-CPP.png)<br>
I then have a Blueprint Library with a function helper functions, including Read Input that calls upon the reflected C++ functions. I also have a pre-path set to the input text files directory so that in each new Day BP I only need to change the file name.
![Read Input BaseLib](https://github.com/JWaters02/AoC-2021/blob/71b4748523fedc471236bfe92ee61b2a52047428/BP%20Solutions/ReadInput-BaseLib.png)
I then have a Base BP Actor that has a couple of variables and nodes already set up. I then can just duplicate the Base BP Actor and build my solutions from there.
![Base BP Actor](https://github.com/JWaters02/AoC-2021/blob/42041b80a35c83fa3429c0b7baf8941574c8d97f/BP%20Solutions/BaseBP.png)
### Day 1
![Day 1](https://github.com/JWaters02/AoC-2021/blob/b031097fba6b9ebfc6a603df9f25ff59810732cd/BP%20Solutions/Day1.png)
### Day 2
![Day 2](https://github.com/JWaters02/AoC-2021/blob/b031097fba6b9ebfc6a603df9f25ff59810732cd/BP%20Solutions/Day2.png)
### Day 3
There were a few different functions for various processes so I took screenshots of the most important ones. The first screenshot is the main function for parts 1 and 2. I wrote the BP code based off my Python solution.
![Day 3 Main](https://github.com/JWaters02/AoC-2021/blob/b031097fba6b9ebfc6a603df9f25ff59810732cd/BP%20Solutions/Day3-Main.png)
This function below counts the number of 1s and 0s in each column and stores them into a struct.
![Day 3 Create Counter](https://github.com/JWaters02/AoC-2021/blob/b031097fba6b9ebfc6a603df9f25ff59810732cd/BP%20Solutions/Day3-CreateCounter.png)
This converts the binary string to a decimal number, since UE does not have a built in function for this.
![Day 3 Binary To Decimal](https://github.com/JWaters02/AoC-2021/blob/b031097fba6b9ebfc6a603df9f25ff59810732cd/BP%20Solutions/Day3-BinToDec.png)
The below function is effectively the main function for part 2, but since it gets called twice for the oxygen and C02 scrubbers I had to make it a separate function.
![Day 3 Get Rating](https://github.com/JWaters02/AoC-2021/blob/b031097fba6b9ebfc6a603df9f25ff59810732cd/BP%20Solutions/Day3-GetRating.png)
This function filters out the lines to determine the sole rating.
![Day 3 Filter Lines](https://github.com/JWaters02/AoC-2021/blob/b031097fba6b9ebfc6a603df9f25ff59810732cd/BP%20Solutions/Day3-FilterLines.png)
### Day 4
Day 4's input is so complex that I just did not want to spend the time to write a solution in BP.
### Day 5
Since parts 1 and 2 were very similar, I was able to put them into the same function with a parameter that checked which part was being run.<br>
![Day 5 Main](https://github.com/JWaters02/AoC-2021/blob/c6495bfba780c18a8f25fcf05df4752fe9ca6d19/BP%20Solutions/Day5-Main.png)<br>
The overall program loop.
![Day 5 Find Vents](https://github.com/JWaters02/AoC-2021/blob/c6495bfba780c18a8f25fcf05df4752fe9ca6d19/BP%20Solutions/Day5-FindVents.png)
This parses the input into the array of structs where element 0 and 1 are integer arrays. This was basically my lists data structure you can see in my Python solution.
![Day 5 Parse Input](https://github.com/JWaters02/AoC-2021/blob/c6495bfba780c18a8f25fcf05df4752fe9ca6d19/BP%20Solutions/Day5-ParseInput.png)
This function sets the x1, x2, y1, y2 values for part 1 plus the dx and dy values for part 2.
![Day 5 Set Coords](https://github.com/JWaters02/AoC-2021/blob/c6495bfba780c18a8f25fcf05df4752fe9ca6d19/BP%20Solutions/Day5-SetCoords.png)
Then it does all checks for line intersections...
![Day 5 Create Grid](https://github.com/JWaters02/AoC-2021/blob/c6495bfba780c18a8f25fcf05df4752fe9ca6d19/BP%20Solutions/Day5-CreateGrid.png)
...and passes them into this function which adds them to a grid - which here is a struct where element 0 is an integer array (stores x, y coordinates) and element 0 is the count of intersections on each coordinate.
![Day 5 Add Line To Grid](https://github.com/JWaters02/AoC-2021/blob/c6495bfba780c18a8f25fcf05df4752fe9ca6d19/BP%20Solutions/Day5-AddLineToGrid.png)
It also has to do an additional check to see if the coordinate already exists in the grid, which then increments the count at that coordinate.
![Day 5 If Coords Exist](https://github.com/JWaters02/AoC-2021/blob/c6495bfba780c18a8f25fcf05df4752fe9ca6d19/BP%20Solutions/Day5-IfCoordsExist.png)
### Day 6
Since parts 1 and 2 were very similar, I was able to put them into the same function with a parameter that checked which part was being run.<br>
![Day 6 Main](https://github.com/JWaters02/AoC-2021/blob/52e4e7cbada8c024f19b26ff7ff90784b1c78954/BP%20Solutions/Day6-Main.png)<br>
First I needed to parse the input into an array. This was actually more difficult than I thought it would be, for whatever reason.
![Day 6 Parse Input](https://github.com/JWaters02/AoC-2021/blob/52e4e7cbada8c024f19b26ff7ff90784b1c78954/BP%20Solutions/Day6-ParseInput.png)
The overall program loop that counts the fish. As you can see, I had to use int64 for the count because I was getting reaching the bit limit. Sometimes doing so much programming in BP breaks my brain and so it took me a solid 10 minutes to figure out how to convert from int64 to string, since UE4 does not have a built in cast for this, and obviously I cannot just convert to int to string as it would hit the bit limit again.
![Day 6 Count Fish](https://github.com/JWaters02/AoC-2021/blob/52e4e7cbada8c024f19b26ff7ff90784b1c78954/BP%20Solutions/Day6-CountFish.png)
This function takes the starting ages and returns the list of fish at the start.
![Day 6 Add Fish](https://github.com/JWaters02/AoC-2021/blob/52e4e7cbada8c024f19b26ff7ff90784b1c78954/BP%20Solutions/Day6-AddFish.png)
### Day7
![Day 7 Main](https://github.com/JWaters02/AoC-2021/blob/dcaceab56567af5d72b11abe93f59746877a7bcf/BP%20Solutions/Day7-Main.png)
At first I thought I could just nick my parse input function from day 6, however I built it assuming that the numbers were all 1 digit, and since day 7 input as numbers of more than 1 digit, I could not use it. I know that I could modify it by 1) checking for the number of characters before the delimeter since last being split c) add those chars to a string 3) converting to an int 4) adding to the int array. However, I couldn't really be bothered and decided to cheat a little by writng a C++ function to do it for me.
![Day 7 Parse Input](https://github.com/JWaters02/AoC-2021/blob/dcaceab56567af5d72b11abe93f59746877a7bcf/BP%20Solutions/Day7-ParseInput.png)
For my solution to work, I needed to sort the array. However, BP does not have a built in sort function, so I had to write my own. I decided to use insertion sort because although it's not the most efficient (O(n^2)), it's the easiest to write - I tried writing quick sort first but my implementation did not work and I couldn't figure out why.
![Day 7 Sort](https://github.com/JWaters02/AoC-2021/blob/e9388e41de65c35bdaeb3e90791de6d46540336b/BP%20Solutions/Day7-Sort.png)
I then just wrote the functions that I have in my Python solution.
![Day 7 Middle](https://github.com/JWaters02/AoC-2021/blob/3984104fe7c1775f96dc6c66cf57f438f789199e/BP%20Solutions/Day7-Middle.png)
![Day 7 Fuel Usage](https://github.com/JWaters02/AoC-2021/blob/e9388e41de65c35bdaeb3e90791de6d46540336b/BP%20Solutions/Day7-FuelUsage.png)
![Day 7 Fuel Cost](https://github.com/JWaters02/AoC-2021/blob/3984104fe7c1775f96dc6c66cf57f438f789199e/BP%20Solutions/Day7-FuelCost.png)
Basically my part 2 solution.
![Day 7 Variable Fuel Usage](https://github.com/JWaters02/AoC-2021/blob/main/BP%20Solutions/Day7-VariableFuelUsage.png)