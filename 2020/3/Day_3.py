'''
--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

Your puzzle answer was 289.

--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

Your puzzle answer was 5522401584.
'''
import math
import numpy as np

def read_file(file_path):
    ip = []
    f = open(file_path,'r')
    for line in f:
        ip.append(list(line.rstrip('\n')))
    f.close()
    return ip

def number_trees(file_path,slopes):
    ip = read_file(file_path)
    num_trees = []
    max_r = len(ip[0])
    max_d= len(ip)
    for slope in slopes:
        r = slope[0]
        d = slope[1]
        repeat_factor = math.ceil((max_d/max_r) * ( r / d ))
        ip_expanded = []
        for elem in ip:
            ip_expanded.append(elem * (repeat_factor))
        max_d_expanded = len(ip_expanded)
        pt_x=0
        pt_y=0
        count = 0
        while(pt_x <= max_d_expanded-1):
            if (ip_expanded[pt_x][pt_y] == '#' ):
                count = count + 1
            pt_x = pt_x + d
            pt_y = pt_y + r
        num_trees.append(count)
        print(count)
    print(f"The product of trees {np.prod(num_trees)}")

if __name__ == '__main__':
    print("\n========= part 1 ===========")
    print("==== for example file ====")
    print(" Right 3, down 1 ")
    file_path = 'example.txt'
    slopes = [(3,1)]
    number_trees(file_path,slopes)
    
    print("\n==== for input file ====")
    print(" Right 3, down 1 ")
    file_path = 'input.txt'
    slopes = [(3,1)]
    number_trees(file_path,slopes)
    
    print("\n========= part 2 ===========")
    print("==== for example file ====")
    print(" Right 1, down 1 \
           \n Right 3, down 1 \
           \n Right 5, down 1 \
           \n Right 7, down 1 \
           \n Right 1, down 2")
    file_path = 'example.txt'
    slopes =[
    (1,1),(3,1),(5,1),(7,1),(1,2)
    ]
    number_trees(file_path,slopes)
    
    print("\n==== for input file ====")
    print(" Right 1, down 1 \
           \n Right 3, down 1 \
           \n Right 5, down 1 \
           \n Right 7, down 1 \
           \n Right 1, down 2" )
    file_path = 'input.txt'
    slopes =[
    (1,1),(3,1),(5,1),(7,1),(1,2)
    ]
    number_trees(file_path,slopes)