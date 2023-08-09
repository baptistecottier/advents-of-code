# Advents of code

Here you can find my solutions for the [Advent of Code](https://adventofcode.com) challenges 🎄⭐️🎅🏻.


### __Python Solutions__

To run solutions, you have to a run a script. You can find a minimal working script as `aoc_mw`. You can then add features as automatic puzzle input download and save (based on a cookie session), answer verification (available only once the puzzle is solved, but may be useful for optimisations), etc...


`aoc_mw` first loads the puzzle input then sends it to the function `preprocessing` who build needed data for solving the puzzle.

Then, preprocessed input is given as input to the function `solver` that yields answers when found. 

In some puzzles, the answer to the second part arises before the answer of the first part. In such cases, the answer is yielded together with the part solved as a tuple `(part, answer)`. 

---
### Scores
- Enter the code `1349697-f730f285` in your [Private Leaderboard Homepage](https://adventofcode.com/2022/leaderboard/private) to integrate my leaderboard.

|Year|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2015|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|
|2016|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|
|2017|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|
|2018|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|☆|⭐️|☆|⭐️|⭐️|⭐️|⭐️|★|⭐️|⭐️|☆|★|
|2019|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|☆|⭐️|⭐️|☆|☆|☆|☆|☆|☆|☆|☆|☆|☆|
|2020|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|★|⭐️|⭐️|⭐️|⭐️|⭐️|★|
|2021|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|★|★|☆|☆|★|
|2022|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|⭐️|★|☆|★|☆|⭐️|⭐️|☆|☆|☆|★|

**Legend** : ☆ -  No part solved | ★ - Part 1 solved | ⭐️ - Both parts solved

----

### Acknowledgments
Thanks [Scotow](https://github.com/scotow) for the initial framework and precious coding advices.
