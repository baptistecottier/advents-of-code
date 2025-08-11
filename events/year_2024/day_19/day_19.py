"""
Advent of Code - Year 2024 - Day 19
https://adventofcode.com/2024/day/19
"""

from functools import lru_cache


def preprocessing(puzzle_input: str) -> tuple[list[str], list[str]]:
    """
    Splits the puzzle input into patterns and designs, returning them as separate lists.
    """
    patterns, designs = puzzle_input.split('\n\n')
    patterns = patterns.split(", ")
    designs = designs.splitlines()
    return patterns, designs


def solver(patterns: list[str], designs: list[str]) -> tuple[int, int]:
    """
    Counts the number of ways each design can be constructed from given patterns and yields the
    count of valid designs and their total ways.

    —————— Exemple —————————————————————————————————————————————————————————————————
    Patterns available: r, wr, b, g, bwu, rb, gb, br
    Desired design: brwrr

    |__ b|rwrr: ✅ b exists as a pattern, we continue.
    |     |__ r|wrr ✅
    |     |     |__ w|rr ❌
    |     |     |__ wr|r ✅
    |     |     |      |__ r| r is in patterns and no stripe remains. 🏆
    |     |     |__ wrr ❌
    |     |__ rw|rr ❌
    |     |__ rwr|r ❌
    |__ br|wrr: ✅ rb is an existing pattern, we continue.
    |      |__ Using dynamic programming, we know the design is doable in one way.🏆
    |__ brw|rr: ❌ brw does not exist, we stop that way here.
    """
    @lru_cache
    def count_design_ways(design):
        ways = design in patterns
        for i in range(1, max_length + 1):
            if design[:i] in patterns:
                ways += count_design_ways(design[i:])
        return ways

    max_length = max(map(len, patterns))
    ways = []
    for design in designs:
        desing_ways = count_design_ways(design)
        if desing_ways:
            ways.append(desing_ways)
    return len(ways), sum(ways)
