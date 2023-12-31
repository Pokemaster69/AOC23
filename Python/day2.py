import sys
import re
import numpy as np

#Open file passed as parameter to the program
def readInput():
    if len(sys.argv)==1:
        print("Missing parameter, use the program like this: python3 day2.py [inputfile]")
        exit()
    try:
        f = open(sys.argv[1])
    except FileNotFoundError:
        print("File not found, check your filename and path and try again.")
        exit()
    return f

#Test if the amount of colored cubes matches the limits given in part 1
def valid(rgb):
    return not (rgb[0]>12 or rgb[1]>13 or rgb[2]>14)

#Count maximum amount of cubes per color per game
def count(line):
    maxrgb = [0,0,0]
    for i in range(len(line)):
        t = line[i].split(", ")
        rgb=[0,0,0]
        for j in t:
            temp = j.split()
            match temp[1]:
                case "red": rgb[0]=int(temp[0])
                case "green": rgb[1]=int(temp[0])
                case "blue": rgb[2]=int(temp[0])
        maxrgb = [max(rgb[0],maxrgb[0]), max(rgb[1],maxrgb[1]), max(rgb[2],maxrgb[2])]
    return maxrgb

#Cleanup the input strings to make the calculations easier
def parse(l):
    line = l.split(":")
    line[0] = re.sub("Game ", "", line[0])
    line[1] = line[1].split("; ")
    return line

#Solve both parts
def solve(f):
    p1 = 0
    p2 = 0
    for line in f.readlines():
        clean = parse(line)
        counts = count(clean[1])
        results = [valid(counts), counts]
        p1+=results[0]*int(clean[0])
        p2+=np.prod(results[1])
    return [p1,p2]

#Print the results
result = solve(readInput())
print("Part1: ", result[0])
print("Part2: ", result[1])