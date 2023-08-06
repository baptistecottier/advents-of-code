# Advents of code

Here you can find my solutions for the [Advent of Code](https://adventofcode.com) challenges 🎄⭐️🎅🏻.


### __Python Solutions__

To run solutions, you have to a run a script. You can find a minimal working script as `aoc_mw`. You can also add features as automatic input download and save using a cookie session, answer verification (available only once the puzzle is solved, but may be useful for optimisations), etc... You can save the script in the `/usr/local/bin/` folder and make it executable from anywhere by running `chmod u+x aoc_mw`. To solve the day `d` of year `y`,run `aoc_mw y d`.


`aoc_mw` first loads the puzzle input then sends it to the function `preprocessing` who build needed data for solving the puzzle.

Then, preprocessed input is given as input to the function `solver` that yields answers when found. 

In some puzzles, the answer to the second part arises before the answer of the first part. In such cases, the answer is yielded together with the part solved as a tuple `(part, answer)`. 


### Acknowledgments
Thanks [Scotow](https://github.com/scotow) for the initial framework and precious coding advices.

### Remarks
- Enter the code `1349697-f730f285` in your [Private Leaderboard Homepage](https://adventofcode.com/2022/leaderboard/private) to integrate my leaderboard.
- Score as of June, 8th:
  - 2015: 50 ⭐️
  - 2016: 50 ⭐️
  - 2017: 50 ⭐️
  - 2018: 39 ⭐️ 
  - 2019: 23 ⭐️ 
  - 2020: 47 ⭐️ 
  - 2021: 42 ⭐️ 
  - 2022: 36 ⭐️
