import ahocorasick

def preprocessing(input):
    automaton = ahocorasick.Automaton()
    patterns = [ "_", "1"  , "2"  , "3"    , "4"   , "5"   , "6"  , "7"    , "8"   , "9",
                 "_", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, key in enumerate(patterns):
        automaton.add_word(key, (idx, key))
    automaton.make_automaton()

    document = list()
    for line in input.splitlines():
        document.append([n for _, (n, _) in automaton.iter(line)])
    return document

def solver(document):
    no_spell = 0
    spell    = 0
    for digits in document:
        spell    += 10 * (digits[0] % 10) + (digits[-1] % 10)
        digits    = [n for n in digits if n < 10]
        no_spell += 10 * (digits[0]) + digits[-1]

    yield no_spell
    yield spell