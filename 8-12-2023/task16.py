file = open('8-12-2023/input.txt', 'r')

instruction = file.readline().strip()

lines = [tuple(item.strip().split(" = ")) for item in file.readlines()][1:]

networks = {}

for line in lines:
    start, end = line
    elements = end.strip('()').split(',')
    result_tuple = tuple(element.strip() for element in elements)
    
    networks[start] = result_tuple


start = []
goal =[]

for key in networks.keys():
    if key[2] == 'A':
        start.append(key)
    elif key[2] == 'Z':
        goal.append(key)



NstepList = []
for item in start:
    step = item
    Nstep = 0
    while step not in goal:
        ins = Nstep % len(instruction)
        left, right = networks[step]
        step =''
        if instruction[ins] == 'L':
            step = left
        else:
            step = right
        Nstep += 1
    NstepList.append(Nstep)

import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_of_array(arr):
    if not arr:
        return 0
    current_lcm = arr[0]
    for num in arr[1:]:
        current_lcm = lcm(current_lcm, num)
    return current_lcm

print(lcm_of_array(NstepList))
    

