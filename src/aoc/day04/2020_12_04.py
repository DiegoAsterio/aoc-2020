def is_valid(passport):
    required_fields = {'byr',
                       'iyr',
                       'eyr',
                       'hgt',
                       'hcl',
                       'ecl',
                       'pid'}
    keys = set()
    kval = dict()
    for x in passport.split(' '):
        k, v = x.split(':')
        keys.add(k.strip())
        kval[k] = v
    if len(required_fields - keys) != 0:
        return False
    else:
        byr = kval['byr']
        if not byr.isdigit() or len(byr) != 4:
            return False
        elif int(byr) < 1920 or  2002 < int(byr):
            return False
        iyr = kval['iyr']
        if not iyr.isdigit() or len(iyr) != 4:
            return False
        elif int(iyr) < 2010 or 2020 < int(iyr):
            return False
        eyr = kval['eyr']
        if not eyr.isdigit() or len(eyr) != 4:
            return False
        elif int(eyr) < 2020 or 2030 < int(eyr):
            return False
        hgt = kval['hgt']
        if not hgt[:-2].isdigit():
            return False
        if hgt[-2:] == "in":
            if int(hgt[:-2]) < 59 or 76 < int(hgt[:-2]):
                return False
        elif hgt[-2:] == "cm":
            if int(hgt[:-2]) < 150 or 193 < int(hgt[:-2]):
                return False
        else:
            return False
        hcl = kval['hcl']
        if hcl[0] != "#":
            return False
        for char in hcl[1:]:
            if char not in "0123456789abcdef":
                return False
        ecl = kval['ecl']
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        pid = kval['pid']
        if not pid.isdigit() or len(pid) != 9:
            return False
    return True
        
def load_passports(path):
    ret = []
    with open(path) as f:
        aux = []
        for line in f:
            if len(line.strip()) == 0:
                ret.append(" ".join(x for x in aux))
                aux = []
            else:
                aux.append(line.strip())
        ret.append(" ".join(x for x in aux))
    return ret

if __name__ == "__main__":
    passports = load_passports("2020_12_04.input")
    count = 0
    for passport in passports:
        if is_valid(passport):
            count += 1
    print("There are {} valid passports".format(count))        
    
