#!/usr/bin/env python
import re

def validate(data):
    count = 0
    mandatory_fields = set(['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'])
    for line in data:
        print(line)
        fields = {x.split(':')[0]: x.split(':')[1] for x in line.split()}
        if mandatory_fields.issubset(fields.keys()):
            # Check Birth Year
            if int(fields['byr']) < 1920 or int(fields['byr']) > 2002:
                print("Invalid Birth Year")
                continue
            # Check Issue Year
            if int(fields['iyr']) < 2010 or int(fields['iyr']) > 2020:
                print("Invalid Issue Year")
                continue
            # Check Expiration Year
            if int(fields['eyr']) < 2020 or int(fields['eyr']) > 2030:
                print("Invalid Expiration Year")
                continue
            # Check Height
            if ''.join(fields['hgt'][-2:]) == 'cm':
                if int(''.join(fields['hgt'][:-2])) < 150 or int(''.join(fields['hgt'][:-2])) > 193:
                    print("Invalid Height")
                    continue
            elif ''.join(fields['hgt'][-2:]) == 'in':
                if int(''.join(fields['hgt'][:-2])) < 59 or int(''.join(fields['hgt'][:-2])) > 76:
                    print("Invalid Height")
                    continue
            else:
                print("Invalid Height")
                continue
            # Check Hair Color
            if not re.match(r"#[A-Fa-f0-9]{6}", fields['hcl']):
                print("Invalid Hair Color")
                continue
            # Check Eye Color
            if fields['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                print("Invalid Eye Color")
                continue
            # Check Passport ID
            if not re.match(r"^[0-9]{9}$", fields['pid']):
                print("Invalid Passport ID")
                continue
            count += 1
        else:
            print('Invalid Mandatory Fields')
    return count


def day4test():
    with open('test.txt') as f:
        data = f.read()
        data = [' '.join(x.strip().split('\n')) for x in data.split('\n\n')]
        print(validate(data))


def day4part1():
    with open('day4.txt') as f:
        data = f.read()
        data = [' '.join(x.strip().split('\n')) for x in data.split('\n\n')]
        print(validate(data))


if __name__=="__main__":
    day4test()
    day4part1()
