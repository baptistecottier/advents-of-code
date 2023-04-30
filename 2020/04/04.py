import string

def generator(input): 
    details = []
    input = input.replace('\n\n','_').replace('\n',' ').replace('_', '\n')
    for passport in input.splitlines():
        infos = {}
        for info in passport.split(' '):
            key, value = info.split(':')
            infos[key]=value
        details.append(infos)
    return details
    
def part_1(input): 
    return sum([is_passport_valid(passport) for passport in input])

def part_2(input):
    return sum([1920 <= int(passport['byr']) <= 2002 and 2010 <= int(passport['iyr']) <= 2020 and 2020 <= int(passport['eyr']) <= 2030 and (('in' in passport['hgt'] and 59 <= int(passport['hgt'][:-2]) <= 76) or ('cm' in passport['hgt'] and 150 <= int(passport['hgt'][:-2]) <= 193)) and (passport['hcl'][0] == '#' and all([c in set(string.hexdigits) for c in passport['hcl'][1:]])) and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and len(passport['pid']) == 9 for passport in input if is_passport_valid(passport)])

def is_passport_valid(passport):
    return len(passport.keys()) == 8 or (len(passport.keys()) == 7 and 'cid' not in passport.keys())