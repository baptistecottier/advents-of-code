## ___Day 16: Reindeer Maze___

It's time again for the [Reindeer <b>O</b>lympics](../../2015/14/14.md#day-14-reindeer-olympics)! This year, the big event is the __Reindeer Maze__, where the Reindeer compete for the __lowest score__.

You and The Historians arrive to search for the Chief right as the event is about to start. It wouldn't hurt to watch a little, right?

The Reindeer start on the Start Tile (marked `S`) facing __East__ and need to reach the End Tile (marked `E`). They can move forward one tile at a time (increasing their score by `1` point), but never into a wall (`#`). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by `1000` points).

To figure out the best place to sit, you start by grabbing a map (your puzzle input) from a nearby kiosk. For example:

```
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
```

There are many paths through this maze, but taking any of the best paths would incur a score of only __`7036`__. This can be achieved by taking a total of `36` steps forward and turning 90 degrees a total of `7` times:


<pre><code>###############
#.......#....<b>E</b>#
#.#.###.#.###<b>^</b>#
#.....#.#...#<b>^</b>#
#.###.#####.#<b>^</b>#
#.#.#.......#<b>^</b>#
#.#.#####.###<b>^</b>#
#..<b>>>>>>>>>v</b>#<b>^</b>#
###<b>^</b>#.#####<b>v</b>#<b>^</b>#
#<b>>>^</b>#.....#<b>v</b>#<b>^</b>#
#<b>^</b>#.#.###.#<b>v</b>#<b>^</b>#
#<b>^</b>....#...#<b>v</b>#<b>^</b>#
#<b>^</b>###.#.#.#<b>v</b>#<b>^</b>#
#<b>S</b>..#.....#<b>>>^</b>#
###############
</code></pre>

Here's a second example:

```
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
```

In this maze, the best paths cost __`11048`__ points; following one such path would look like this:

<pre><code>#################
#...#...#...#..<b>E</b>#
#.#.#.#.#.#.#.#<b>^</b>#
#.#.#.#...#...#<b>^</b>#
#.#.#.#.###.#.#<b>^</b>#
#<b>>>v</b>#.#.#.....#<b>^</b>#
#<b>^</b>#<b>v</b>#.#.#.#####<b>^</b>#
#<b>^</b>#<b>v</b>..#.#.#<b>>>>>^</b>#
#<b>^</b>#<b>v</b>#####.#<b>^</b>###.#
#<b>^</b>#<b>v</b>#..<b>>>>>^</b>#...#
#<b>^</b>#<b>v</b>###<b>^</b>#####.###
#<b>^</b>#<b>v</b>#<b>>>^</b>#.....#.#
#<b>^</b>#<b>v</b>#<b>^</b>#####.###.#
#<b>^</b>#<b>v</b>#<b>^</b>........#.#
#<b>^</b>#<b>v</b>#<b>^</b>#########.#
#<b>S</b>#<b>>>^</b>..........#
#################
</code></pre>

Note that the path shown above includes one 90 degree turn as the very first move, rotating the Reindeer from facing East to facing North.

Analyze your map carefully. __What is the lowest score a Reindeer could possibly get?__

## ___Part Two___

Now that you know what the best paths look like, you can figure out the best spot to sit.

Every non-wall tile (`S`, `.`, or `E`) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is __whether the tile is on one of the best paths through the maze__. If you sit somewhere else, you'd miss all the action!

So, you'll need to determine which tiles are part of __any__ best path through the maze, including the `S` and `E` tiles.

In the first example, there are __`45`__ tiles (marked `O`) that are part of at least one of the various best paths through the maze:

<pre><code>###############
#.......#....<b>O</b>#
#.#.###.#.###<b>O</b>#
#.....#.#...#<b>O</b>#
#.###.#####.#<b>O</b>#
#.#.#.......#<b>O</b>#
#.#.#####.###<b>O</b>#
#..<b>OOOOOOOOO</b>#<b>O</b>#
###<b>O</b>#<b>O</b>#####<b>O</b>#<b>O</b>#
#<b>OOO</b>#<b>O</b>....#<b>O</b>#<b>O</b>#
#<b>O</b>#<b>O</b>#<b>O</b>###.#<b>O</b>#<b>O</b>#
#<b>OOOOO</b>#...#<b>O</b>#<b>O</b>#
#<b>O</b>###.#.#.#<b>O</b>#<b>O</b>#
#<b>O</b>..#.....#<b>OOO</b>#
###############
</code></pre>

In the second example, there are __`64`__ tiles that are part of at least one of the best paths:

<pre><code>#################
#...#...#...#..<b>O</b>#
#.#.#.#.#.#.#.#<b>O</b>#
#.#.#.#...#...#<b>O</b>#
#.#.#.#.###.#.#<b>O</b>#
#<b>OOO</b>#.#.#.....#<b>O</b>#
#<b>O</b>#<b>O</b>#.#.#.#####<b>O</b>#
#<b>O</b>#<b>O</b>..#.#.#<b>OOOOO</b>#
#<b>O</b>#<b>O</b>#####.#<b>O</b>###<b>O</b>#
#<b>O</b>#<b>O</b>#..<b>OOOOO</b>#<b>OOO</b>#
#<b>O</b>#<b>O</b>###<b>O</b>#####<b>O</b>###
#<b>O</b>#<b>O</b>#<b>OOO</b>#..<b>OOO</b>#.#
#<b>O</b>#<b>O</b>#<b>O</b>#####<b>O</b>###.#
#<b>O</b>#<b>O</b>#<b>OOOOOOO</b>..#.#
#<b>O</b>#<b>O</b>#<b>O</b>#########.#
#<b>O</b>#<b>OOO</b>..........#
#################
</code></pre>

Analyze your map further. __How many tiles are part of at least one of the best paths through the maze?__