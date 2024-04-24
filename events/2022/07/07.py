def preprocessing(puzzle_input): 
    sizes = {}
    path  = ["root"]
    for command in puzzle_input.splitlines():
        details = command.split(' ')
        match details: 
            case ["$", "cd", "/"] : path = ["root"]
            case ["$", "cd", ".."]: path.pop()
            case ["$", "cd", _]   : path.append("".join(path) + details[2])
            case ["dir", _]       : pass 
            case ["$", "ls"]      : pass 
            case _                : 
                for folder in path: 
                    if folder in sizes: 
                        sizes[folder] += int(details[0])
                    else: 
                        sizes[folder] = int(details[0])
    return sorted(sizes.values())


def solver(sizes):
    small_sizes = 0
    root_size = sizes.pop()
    for size in sizes:
        if size <= 100_000: 
            small_sizes += size
        if size > (root_size - 40_000_000): 
            break
    yield small_sizes
    yield size