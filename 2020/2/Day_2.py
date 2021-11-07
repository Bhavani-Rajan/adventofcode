'''
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; 
the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. 
"Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: 
some of the passwords wouldn't have been allowed by 
the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, 
they have created a list (your puzzle input) of passwords 
(according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times 
a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. 
The middle password, cdefg, is not; 
it contains no instances of b, but needs at least 1. 
The first and third passwords are valid: 
they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---
While it appears you validated the passwords correctly, 
they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained 
the password policy rules from his old job at the sled rental place down the street! 
The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, 
where 1 means the first character, 2 means the second character, 
and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
'''
import pandas as pd
import numpy as np

def split_string(s):
    subs = s.split(":")
    string = subs[1].strip()
    vals = subs[0].split(' ')
    letter = vals[1]
    vals = vals[0].split('-')
    lo_limit = vals[0]
    hi_limit = vals[1]
    
    return pd.Series([string, letter, lo_limit, hi_limit])

def is_pwd_1(s,letter, lo_limit, hi_limit):
    rt = 0
    found = s.count(letter)
    if ((found >= lo_limit) and (found <= hi_limit)):
        rt = 1
    return rt

def part_1(pwd):
    pwd[['string', 'letter', 'lo_limit', 'hi_limit']] = pwd[0].apply(split_string)
    pwd['lo_limit'] = pwd['lo_limit'].astype(int)
    pwd['hi_limit'] = pwd['hi_limit'].astype(int)
    pwd['is_pwd'] = np.vectorize(is_pwd_1)(pwd['string'],pwd['letter'],pwd['lo_limit'],pwd['hi_limit'])
    print(pwd['is_pwd'].sum())

def is_pwd_2(s,letter, lo_limit, hi_limit):
    rt = 0
    lo_flag = (s[lo_limit - 1] == letter)
    hi_flag = (s[hi_limit - 1] == letter)
    if ( lo_flag ^ hi_flag ):
        rt = 1
    return rt
    
def part_2(pwd):
    pwd[['string', 'letter', 'lo_limit', 'hi_limit']] = pwd[0].apply(split_string)
    pwd['lo_limit'] = pwd['lo_limit'].astype(int)
    pwd['hi_limit'] = pwd['hi_limit'].astype(int)
    pwd['is_pwd'] = np.vectorize(is_pwd_2)(pwd['string'],pwd['letter'],pwd['lo_limit'],pwd['hi_limit'])
    print(pwd['is_pwd'].sum())
    
if __name__ == '__main__':
    # To test with example
    l = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
    ]
    print(l)
    pwd = pd.DataFrame(l)
    print(f" Part 1 for the sample {l}")
    part_1(pwd)
    print(f" Part 2 for the sample {l}")
    part_2(pwd)
    
    pwd = pd.read_csv("./input.csv", header=None)
    print(f" Count of correct passwords Part 1 for the input file")
    part_1(pwd)
    print(f" Count of correct passwordsPart 2 for the input file")
    part_2(pwd)