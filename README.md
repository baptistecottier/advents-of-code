# Advents of code

Here you can find my solutions for the [Advent of Code](https://adventofcode.com) challenges 🎄★🎅🏻.


### __Python Solutions__

To run solutions, you have to a run a script. You can find a minimal working script as `aoc_mw`. You can then add features as automatic puzzle input download and save (based on a cookie session), answer verification (available only once the puzzle is solved, but may be useful for optimisations), etc...


`aoc_mw` first loads the puzzle input then sends it to the function `preprocessing` who build needed data for solving the puzzle.

Then, preprocessed input is given as input to the function `solver` that yields answers when found. 

In some puzzles, the answer to the second part arises before the answer of the first part. In such cases, the answer is yielded together with the part solved as a tuple `(part, answer)`. 

---
### Scores

Enter the code `1349697-f730f285` in your [Private Leaderboard Homepage](https://adventofcode.com/2022/leaderboard/private) if you wish to integrate my leaderboard.

<div align="center">

|   |2015|2016|2017|2018|2019|2020|2021|2022|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 01 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/01)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/01)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/01)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/01)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/01)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/01)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/01)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/01)
| 02 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/02)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/02)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/02)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/02)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/02)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/02)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/02)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/02)
| 03 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/03)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/03)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/03)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/03)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/03)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/03)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/03)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/03)
| 04 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/04)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/04)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/04)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/04)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/04)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/04)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/04)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/04)
| 05 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/05)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/05)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/05)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/05)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/05)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/05)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/05)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/05)
| 06 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/06)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/06)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/06)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/06)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/06)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/06)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/06)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/06)
| 07 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/07)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/07)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/07)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/07)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/07)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/07)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/07)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/07)
| 08 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/08)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/08)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/08)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/08)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/08)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/08)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/08)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/08)
| 09 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/09)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/09)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/09)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/09)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/09)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/09)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/09)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/09)
| 10 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/10)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/10)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/10)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/10)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/10)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/10)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/10)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/10)
| 11 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/11)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/11)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/11)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/11)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/11)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/11)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/11)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/11)
| 12 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/12)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/12)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/12)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/12)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/12)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/12)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/12)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/12)
| 13 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/13)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/13)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/13)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/13)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/13)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/13)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/13)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/13)
| 14 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/14)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/14)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/14)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/14)||[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/14)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/14)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/14)
| 15 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/15)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/15)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/15)||[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/15)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/15)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2021/15)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/15)
| 16 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/16)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/16)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/16)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/16)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/14)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/16)||
| 17 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/17)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/17)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/17)||[☆](https://github.com/baptistecottier/advents-of-code/tree/main/2019/17)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/17)||
| 18 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/18)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/18)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/18)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/18)||[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/18)||[☆](https://github.com/baptistecottier/advents-of-code/tree/main/2022/18)
| 19 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/19)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/19)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/19)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/19)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2019/19)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/19)||
| 20 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/20)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/20)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/20)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/20)||[☆](https://github.com/baptistecottier/advents-of-code/tree/main/2020/20)||[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/20)
| 21 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/21)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/21)|[★<sup>⌛</sup>](https://github.com/baptistecottier/advents-of-code/tree/main/2017/21)|[☆](https://github.com/baptistecottier/advents-of-code/tree/main/2018/21)||[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/21)||[★](https://github.com/baptistecottier/advents-of-code/tree/main/2022/21)
| 22 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/22)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/22)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/22)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/22)||[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/22)||
| 23 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/23)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/23)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/23)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/23)||[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/23)||
| 24 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/24)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/24)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/24)|||[★](https://github.com/baptistecottier/advents-of-code/tree/main/2020/24)||
| 25 |[★](https://github.com/baptistecottier/advents-of-code/tree/main/2015/25)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2016/25)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2017/25)|[★](https://github.com/baptistecottier/advents-of-code/tree/main/2018/25)||[☆](https://github.com/baptistecottier/advents-of-code/tree/main/2020/25)||[☆](https://github.com/baptistecottier/advents-of-code/tree/main/2022/25)

</div>

☆ - Part 1 solved

★ - Both parts solved

⌛- Slow solution

----

### Acknowledgments
Thanks [Scotow](https://github.com/scotow) for the initial framework and precious coding advices.
