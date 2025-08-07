# ***Day 18: Snailfish***

You descend into the ocean trench and encounter some [snailfish](https://en.wikipedia.org/wiki/Snailfish). They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his **math homework**.

Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a **pair** - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.

Pairs are written as <code>[x,y]</code>, where `x` and `y` are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:

<pre><code>[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
</code></pre>

This snailfish homework is about **addition**. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, <code>[1,2]</code> + <code>[[3,4],5]</code> becomes <code>[[1,2],[[3,4],5]]</code>.

There's only one problem: **snailfish numbers must always be reduced**, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

To **reduce a snailfish number**, you must repeatedly do the first action in this list that applies to the snailfish number:

- If any pair is **nested inside four pairs**, the leftmost such pair **explodes**.
- If any regular number is **10 or greater**, the leftmost such regular number **splits**.

Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if **split** produces a pair that meets the **explode** criteria, that pair **explodes** before other **splits** occur.

To **explode** a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number `0`.

Here are some examples of a single explode action:

- <code>[[[[<b>[9,8]</b>,1],2],3],4]</code> becomes <code>[[[[<b>0</b>,<b>9</b>],2],3],4]</code> (the `9` has no regular number to its left, so it is not added to any regular number).
- <code>[7,[6,[5,[4,<b>[3,2]</b>]]]]</code> becomes <code>[7,[6,[5,[<b>7</b>,<b>0</b>]]]]</code> (the `2` has no regular number to its right, and so it is not added to any regular number).
- <code>[[6,[5,[4,<b>[3,2]</b>]]],1]</code> becomes <code>[[6,[5,[<b>7</b>,<b>0</b>]]],<b>3</b>]</code>.
- <code>[[3,[2,[1,<b>[7,3]</b>]]],[6,[5,[4,[3,2]]]]]</code> becomes <code>[[3,[2,[<b>8</b>,<b>0</b>]]],[<b>9</b>,[5,[4,[3,2]]]]]</code> (the pair <code>[3,2]</code> is unaffected because the pair <code>[7,3]</code> is further to the left; <code>[3,2]</code> would explode on the next action).
- <code>[[3,[2,[8,0]]],[9,[5,[4,<b>[3,2]</b>]]]]</code> becomes <code>[[3,[2,[8,0]]],[9,[5,[<b>7</b>,<b>0</b>]]]]</code>.

To **split** a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded **down**, while the right element of the pair should be the regular number divided by two and rounded **up**. For example, `10` becomes <code>[5,5]</code>, `11` becomes <code>[5,6]</code>, `12` becomes <code>[6,6]</code>, and so on.

Here is the process of finding the reduced result of <code>[[[[4,3],4],4],[7,[[8,4],9]]]</code> + <code>[1,1]</code>:

<pre><code>after addition: [[[[<b>[4,3]</b>,4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[<b>[8,4]</b>,9]]],[1,1]]
after explode:  [[[[0,7],4],[<b>15</b>,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,<b>13</b>]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,<b>[6,7]</b>]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
</code></pre>

Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: <code>[[[[0,7],4],[[7,8],[6,0]]],[8,1]]</code>.

The homework assignment involves adding up a **list of snailfish numbers** (your puzzle input). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.

For example, the final sum of this list is <code>[[[[1,1],[2,2]],[3,3]],[4,4]]</code>:

<pre><code>[1,1]
[2,2]
[3,3]
[4,4]
</code></pre>

The final sum of this list is <code>[[[[3,0],[5,3]],[4,4]],[5,5]]</code>:

<pre><code>[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
</code></pre>

The final sum of this list is <code>[[[[5,0],[7,4]],[5,5]],[6,6]]</code>:

<pre><code>[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
</code></pre>

Here's a slightly larger example:

<pre><code>[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
</code></pre>

The final sum <code>[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]</code> is found after adding up the above snailfish numbers:

<pre><code>  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
= [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
= [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

  [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
+ [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
= [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

  [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
+ [7,[5,[[3,8],[1,4]]]]
= [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
+ [[2,[2,2]],[8,[8,1]]]
= [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

  [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
+ [2,9]
= [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

  [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
+ [1,[[[9,3],9],[[9,0],[0,7]]]]
= [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

  [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
+ [[[5,[7,4]],7],1]
= [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

  [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
+ [[[[4,2],2],6],[8,7]]
= [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
</code></pre>

To check whether it's the right answer, the snailfish teacher only checks the **magnitude** of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

For example, the magnitude of <code>[9,1]</code> is <code>3*9 + 2*1 = **29**</code>; the magnitude of <code>[1,9]</code> is <code>3*1 + 2*9 = **21**</code>. Magnitude calculations are recursive: the magnitude of <code>[[9,1],[1,9]]</code> is <code>3*29 + 2*21 = **129**</code>.

Here are a few more magnitude examples:

- <code>[[1,2],[[3,4],5]]</code> becomes **`143`**.
- <code>[[[[0,7],4],[[7,8],[6,0]]],[8,1]]</code> becomes **`1384`**.
- <code>[[[[1,1],[2,2]],[3,3]],[4,4]]</code> becomes **`445`**.
- <code>[[[[3,0],[5,3]],[4,4]],[5,5]]</code> becomes **`791`**.
- <code>[[[[5,0],[7,4]],[5,5]],[6,6]]</code> becomes **`1137`**.
- <code>[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]</code> becomes **`3488`**.

So, given this example homework assignment:

<pre><code>[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
</code></pre>

The final sum is:

<pre><code>[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
</code></pre>

The magnitude of this final sum is **`4140`**.

Add up all of the snailfish numbers from the homework assignment in the order they appear. **What is the magnitude of the final sum?**

## ***Part Two***

You notice a second question on the back of the homework assignment:

What is the largest magnitude you can get from adding only two of the snailfish numbers?

Note that snailfish addition is not [commutative](https://en.wikipedia.org/wiki/Commutative_property) - that is, `x + y` and `y + x` can produce different results.

Again considering the last example homework assignment above:

<pre><code>[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
</code></pre>

The largest magnitude of the sum of any two snailfish numbers in this list is **`3993`**. This is the magnitude of <code>[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]</code> + <code>[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]</code>, which reduces to <code>[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]</code>.

**What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?**
 