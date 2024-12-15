# ___Day 15: Warehouse Woes___

You appear back inside your own mini submarine! Each Historian drives their mini submarine in a different direction; maybe the Chief has his own submarine down here somewhere as well?

You look up to see a vast school of [lanternfish](../../2021/06/06.md#day-6-lanternfish) swimming past you. On closer inspection, they seem quite anxious, so you drive your mini submarine over to see if you can help.

Because lanternfish populations grow rapidly, they need a lot of food, and that food needs to be stored somewhere. That's why these lanternfish have built elaborate warehouse complexes operated by robots!

These lanternfish seem so anxious because they have lost control of the robot that operates one of their most important warehouses! It is currently running amok, pushing around boxes in the warehouse with no regard for lanternfish logistics __or__ lanternfish inventory management strategies.

Right now, none of the lanternfish are brave enough to swim up to an unpredictable robot so they could shut it off. However, if you could anticipate the robot's movements, maybe they could find a safe option.

The lanternfish already have a map of the warehouse and a list of movements the robot will __attempt__ to make (your puzzle input). The problem is that the movements will sometimes fail as boxes are shifted around, making the actual movements of the robot difficult to predict.

For example:

```
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
```

As the robot (`@`) attempts to move, if there are any boxes (`O`) in the way, the robot will also attempt to push those boxes. However, if this action would cause the robot or a box to move into a wall (`#`), nothing moves instead, including the robot. The initial positions of these are shown on the map at the top of the document the lanternfish gave you.

The rest of the document describes the __moves__ (`^` for up, `v` for down, `<` for left, `>` for right) that the robot will attempt to make, in order. (The moves form a single giant sequence; they are broken into multiple lines just to make copy-pasting easier. Newlines within the move sequence should be ignored.)

Here is a smaller example to get started:

```
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
```

Were the robot to attempt the given sequence of moves, it would push around the boxes as follows:

<pre><code>Initial state:
########
#..O.O.#
##<b>@</b>.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##<b>@</b>.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.<b>@</b>O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.<b>@</b>O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..<b>@</b>OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...<b>@</b>OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...<b>@</b>OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..<b>@</b>..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..<b>@</b>..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.<b>@</b>...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..<b>@</b>O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...<b>@</b>O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....<b>@</b>O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O<b>@</b>.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O<b>@</b>..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O<b>@</b>..#
#...O..#
#...O..#
########
</code></pre>

The larger example has many more moves; after the robot has finished those moves, the warehouse would look like this:

<pre><code>
##########
#.O.O.OOO#
#........#
#OO......#
#OO<b>@</b>.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
</code></pre>

The lanternfish use their own custom Goods Positioning System (GPS for short) to track the locations of the boxes. The __GPS coordinate__ of a box is equal to 100 times its distance from the top edge of the map plus its distance from the left edge of the map. (This process does not stop at wall tiles; measure all the way to the edges of the map.)

So, the box shown below has a distance of `1` from the top edge of the map and `4` from the left edge of the map, resulting in a GPS coordinate of `100 * 1 + 4 = 104`.

```
#######
#...O..
#......
```

The lanternfish would like to know the __sum of all boxes' GPS coordinates__ after the robot finishes moving. In the larger example, the sum of all boxes' GPS coordinates is __`10092`__. In the smaller example, the sum is __`2028`__.

Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, __what is the sum of all boxes' GPS coordinates?__

## ___Part Two___

The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a __second__ warehouse's robot is __also__ malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference: everything except the robot is __twice as wide__! The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:

*   If the tile is `#`, the new map contains `##` instead.
*   If the tile is `O`, the new map contains `[]` instead.
*   If the tile is `.`, the new map contains `..` instead.
*   If the tile is `@`, the new map contains `@.` instead.

This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by `[]`. (The robot does not change size.)

The larger example from before would now look like this:

```
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
```

Because boxes are now twice as wide but the robot is still the same size and speed, boxes can be aligned such that they directly push two other boxes at once. For example, consider this situation:

```
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
```

After appropriately resizing this map, the robot would push around these boxes as follows:

<pre><code>Initial state:
##############
##......##..##
##..........##
##....[][]<b>@</b>.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]<b>@</b>..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].<b>@</b>..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......<b>@</b>..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......<b>@</b>...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....<b>@</b>....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....<b>@</b>....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....<b>@</b>....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....<b>@</b>.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...<b>@</b>......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...<b>@</b>[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...<b>@</b>.[]...##
##....[]....##
##..........##
##..........##
##############
</code></pre>

This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question. So, the box shown below has a distance of `1` from the top edge of the map and `5` from the left edge of the map, resulting in a GPS coordinate of `100 * 1 + 5 = 105`.

```
##########
##...[]...
##........
```

In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:

<pre><code>####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..<b>@</b>......[].[][]##
##......[][]..[]..##
####################
</code></pre>

The sum of these boxes' GPS coordinates is __`9021`__.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. __What is the sum of all boxes' final GPS coordinates?__