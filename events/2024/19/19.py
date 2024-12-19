from functools import lru_cache

def preprocessing(puzzle_input):
    """
    Classical parsing. The first part of the input corresponding to the patterns is
    split using the comma delimiter while the second part, the desired designs, are 
    split line by line.
    """
    patterns, designs = puzzle_input.split('\n\n')
    patterns = patterns.split(", ")
    designs = designs.splitlines()
    return patterns, designs

def solver(patterns, designs):
    """
    To denombrate the different ways to make each design we first look the expected 
    design up to the i-th stripe for i going from 1 to the longest pattern length. 
    If the obtained pattern exists, we recursively apply the function, until no more
    pattern is detected and in that case, the way to make the design is dropped, 
    otherwise, we end by getting a whole design that is a pattern and this counts as
    a new way to make the design. We the store the number of ways to achieve a 
    design if that number is non zero. 
    
    Answer to first part is given by counting the number of elements stored.
    Answer to seconf part is obtained by summing those elements.
    
    
    —————— Exemple —————————————————————————————————————————————————————————————————
    Patterns available: r, wr, b, g, bwu, rb, gb, br
    Desired design: brwrr
    
    |__ b|rwrr: ✅ b exists as a pattern, we continue.
    |     |__ r|wrr ✅ 
    |     |     |__ w|rr ❌
    |     |     |__ wr|r ✅
    |     |     |      |__ r| r is in patterns and no stripe remains. 🏆 
    |     |     |__ wrr    ❌
    |     |__ rw|rr ❌
    |     |__ rwr|r ❌
    |__ br|wrr: ✅ rb is an existing pattern, we continue.
    |      |__ Using dynamic programming, we know the pattern is doable in one way.🏆
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

    ways = list()
    for design in designs:
        desing_ways = count_design_ways(design)
        if desing_ways: ways.append(desing_ways)
    yield len(ways)
    yield sum(ways)