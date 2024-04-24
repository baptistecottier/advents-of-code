import string


def preprocessing(puzzle_input): 
    details = []
    for passport in puzzle_input.split('\n\n'):
        passport = passport.replace('\n', ' ')
        infos = {}
        for info in passport.split(' '):
            key, value = info.split(':')
            infos[key]=value
        details.append(infos)
    return details


def solver(passports): 
    candidates = 0
    valids = 0
    for passport in passports:
        if is_passport_valid(passport): 
            candidates += 1
            if are_fields_valids(passport): valids += 1
    yield candidates
    yield valids


def are_fields_valids(passport):
    return      1920 <= int(passport['byr']) <= 2002 \
            and 2010 <= int(passport['iyr']) <= 2020 \
            and 2020 <= int(passport['eyr']) <= 2030 \
            and (   ('in' in passport['hgt'] and 59 <=  int(passport['hgt'][:-2]) <= 76) \
                 or ('cm' in passport['hgt'] and 150 <= int(passport['hgt'][:-2]) <= 193)) \
            and (passport['hcl'][0] == '#' and all(c in string.hexdigits for c in passport['hcl'][1:])) \
            and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] \
            and len(passport['pid']) == 9


def is_passport_valid(passport):
    return len(passport.keys()) == 8 or (len(passport.keys()) == 7 and 'cid' not in passport.keys())