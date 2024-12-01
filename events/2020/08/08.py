def preprocessing(puzzle_input: str) -> list[int, int]:
    instructions = []
    for instruction in puzzle_input.splitlines():        
        ins, step = instruction.split(' ')
        match ins:
            case 'nop': instructions.append((0, int(step)))
            case 'acc': instructions.append((1, int(step)))
            case 'jmp': instructions.append((2, int(step)))
    return instructions


def solver(program: list[int, int]):
    yield test_program(program)[1]
    
    for modif in range(len(program)):
        ins, value = program[modif]
        if ins == 1: continue
        program[modif] = (2 - ins, value)
        code, acc = test_program(program)
        if code == "halt": 
            yield acc
            break
        program[modif] = (ins, value)

        
def test_program(program: list[int, int]) -> int:
    acc     = 0
    index   = 0 
    visited = set()
    while True:
        if index in visited:
            return ["loop", acc]
        elif index == len(program): 
            return ["halt", acc]
        else: 
            visited.add(index)
            ins, value = program[index]
            match ins:
                case 1: acc   += value
                case 2: index += value - 1
            index += 1