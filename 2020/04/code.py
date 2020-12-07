with open('input.txt') as f:
    lines = f.readlines()

# process file
passports = []
passport = {}
for line in lines:
    if line == '\n':
        passports.append(passport)
        passport = {}
        continue

    items = line.split(' ')
    for item in items:
        key, val = item.split(':')
        passport[key] = val.strip('\n')

# since last line is not empty, add final passport
passports.append(passport)

# part 1
ans1 = 0
for passport in passports:
    valid = len(passport) == 8
    valid |= (len(passport) == 7) and ('cid' not in passport.keys())
    ans1 += valid


# part 2
def valid_year(val, low, high):
    return len(val) == 4 and low <= int(val) <= high


def valid_haircolor(val):
    check = val[0] == '#'
    check &= len(val) == 7
    check &= all([char.isdigit() or char in 'abcdef' for char in val[1:]])
    return check


def valid_pid(val):
    return len(val) == 9 and all([char.isdigit() for char in val])


ans2 = 0
eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for passport in passports:
    valid = len(passport) == 8
    valid |= (len(passport) == 7) and ('cid' not in passport.keys())
    if valid:
        # check years
        valid &= valid_year(passport['byr'], 1920, 2002)
        valid &= valid_year(passport['iyr'], 2010, 2020)
        valid &= valid_year(passport['eyr'], 2020, 2030)

        # check height
        if 'in' in passport['hgt']:
            valid &= 59 <= float(passport['hgt'].strip('in')) <= 76
        elif 'cm' in passport['hgt']:
            valid &= 150 <= float(passport['hgt'].strip('cm')) <= 193
        else:
            valid &= False

        # check hair color
        valid &= valid_haircolor(passport['hcl'])

        # check eye color
        valid &= passport['ecl'] in eyecolors

        # check passport number
        valid &= valid_pid(passport['pid'])

    ans2 += valid

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer))
