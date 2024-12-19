from functools import lru_cache

def preprocessing(puzzle_input):
    patterns, designs = puzzle_input.split('\n\n')
    patterns = patterns.split(", ")
    designs = designs.splitlines()
    return patterns, designs

def solver(patterns, designs):
    @lru_cache
    def count_design_ways(design):
        return (design in patterns) + \
                sum(count_design_ways(design[i:])         \
                        for i in range(1, max_length + 1) \
                            if design[:i] in patterns)
                
    max_length = max(len(pattern) for pattern in patterns)
    doable_designs = 0
    total_ways = 0
    for design in designs:
        ways = count_design_ways(design) 
        total_ways += ways
        doable_designs += ways > 0
    yield doable_designs
    yield total_ways