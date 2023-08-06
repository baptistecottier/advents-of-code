# Advents of code

Here you can find my solutions for the [Advent of Code](https://adventofcode.com) challenges 🎄⭐️🎅🏻.


### __Python Solutions__

To run solutions, you have to a run a script. You can find a minimal working script as `aoc_mw`. You can also add features as automatic input download and save using a cookie session, answer verification (available only once the puzzle is solved, but may be useful for optimisations), etc... You can save the script in the `/usr/local/bin/` folder and make it executable from anywhere by running `chmod u+x aoc_mw`. To solve the day `d` of year `y`,run `aoc_mw y d`.

![image](/Users/baptistecottier/Downloads/carbon.svg)

`aoc_mw` first loads the puzzle input then sends it to the function `preprocessing` who build needed data for solving the puzzle.

Then, preprocessed input is given as input to the function `solver` that yields answers when found. 

In some puzzles, the answer to the second part arises before the answer of the first part. In such cases, the answer is yielded together with the part solved as a tuple `(part, answer)`. 