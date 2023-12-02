file1 = open('2-12-2023/input.txt', 'r')
import numpy 
# target = {"red":12, "green":13, "blue":14}

def find_minimum_set(game:[str])->int:
    minSet = {}
    for set in game:
        parts = set.split(", ")
        for part in parts:
            part_split = part.split()
            color = part_split[1]
            number = part_split[0]
            if color not in minSet:
                minSet[color]= int(number)
            elif minSet[color] < int(number):
                minSet[color]= int(number)
    print(minSet.values())
    return numpy.prod(list(minSet.values()))


counter = 0
res = 0
Lines = file1.readlines()
for line in Lines:
    # print("{}".format( line.strip()))
    counter = counter + 1
    temp =  line.strip()
    
    counterStr = "Game " + str(counter) + ": "
    temp = temp.replace(counterStr,"").split(";")
    val = find_minimum_set(temp)
    res += val
    print(temp)

print(res)

