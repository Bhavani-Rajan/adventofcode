'''
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
'''
import pandas as pd
from itertools import combinations

def mult_2_2020(l):
    '''
    Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

    For example, suppose your expense report contained the following:
    1721
    979
    366
    299
    675
    1456
    In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

    Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
    '''
    total = 2020
    dict_l = {}
    for elem in l:
        dict_l[elem] = total - elem
    for elem in dict_l.values():
        if elem in dict_l.keys():
            print("The product of the two entries that sum to 2020:")
            print(f"{elem} x {dict_l[elem]} = {elem * dict_l[elem]}")
            break
            
def mult_3_2020(l):
    '''
The Elves in accounting are thankful for your help; 
one of them even offers you a starfish coin they had left over from a past vacation. 
They offer you a second one 
if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. 
Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

    '''
    total = 2020
    comb_l = list(combinations(l,3))
    for elem in comb_l:
        if sum(elem) == total:
            print("The product of the three entries that sum to 2020:")
            print(f"{elem[0]} X {elem[1]} X {elem[2]} = {elem[0] * elem[1] * elem[2]}")
            break;

if __name__ == '__main__':
    # To test with example
    print("Reading from the example")
    l =[1721,
        979,
        366,
        299,
        675,
        1456]
    mult_2_2020(l)
    mult_3_2020(l)
    print("")
    print("reading from the input file")
    ip = pd.read_csv("./input.csv", header=None)
    l = ip[0].to_list()
    mult_2_2020(l)
    mult_3_2020(l)
    