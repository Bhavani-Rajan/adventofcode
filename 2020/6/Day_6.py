'''
--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

Your puzzle answer was 6683.

--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

Your puzzle answer was 3122.

'''
def read_input(file_path):
    rt_list = []
    list_grp = []
    f = open(file_path,'r')
    for line in f:
        if line != "\n" :
            list_grp.append(line.rstrip('\n'))
        if line == "\n":
            rt_list.append(list_grp)
            list_grp = []
    rt_list.append(list_grp)
    f.close()
    return rt_list

def wrangle_list_1(l):
    '''
    set(list('abcab')) -- set(['a','b','c','a','b'])
    '''
    rt_list = []
    for elem in l:
        val = "".join(elem)
        rt_list.append(len(set(list(val))))
#     print(sum(rt_list))
    return sum(rt_list)

def wrangle_list_2(l):
    '''
    from the list of grps,
    sort the elements in each grp by length of the element
    make that separate list of chars to check against all the elements of a group
    maximum count can be the length of the first element as the list is sorted.
    decrease the count if the chk_elem is not part of the elem of a grp and exit the loop
    '''
    list_cnt = []
    for grp in l:
        sl=sorted(grp, key=len)
        chk = list(sl[0])
        cnt = len(chk)
        for chk_elem in chk:
            for elem in sl:
                if chk_elem not in elem:
                    cnt = cnt - 1
                    break
            
        list_cnt.append(cnt)
    return sum(list_cnt)

if __name__ == '__main__':
    l = read_input("example.txt")
    l = read_input("input.txt")
    print("======= part 1 ========")
    cnt = wrangle_list_1(l)
    print(f"The sum of the counts : {cnt}")
    print("======= part 2 ========")
    cnt = wrangle_list_2(l)
    print(f"The sum of the counts everyone answered yes : {cnt}")