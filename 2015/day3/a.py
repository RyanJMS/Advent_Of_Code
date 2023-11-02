import numpy as np
from collections import Counter
f = open('input.txt')
puzzle = f.read()
f.close()

def calc_houses(input):
    visited_houses = set()
    x, y = 0,0
    visited_houses.add((x, y))
    for i in input:
        if i == "<":
            x -= 1
        if i == ">":
            x += 1
        if i == "^":
            y += 1
        if i == "v":
            y -= 1
        visited_houses.add((x, y))
    print(len(visited_houses))

    
        
calc_houses(puzzle)