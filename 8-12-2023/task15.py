file = open('8-12-2023/input.txt', 'r')

instruction = file.readline().strip()

lines = [tuple(item.strip().split(" = ")) for item in file.readlines()][1:]

networks = {}

for line in lines:
    start, end = line
    elements = end.strip('()').split(',')
    result_tuple = tuple(element.strip() for element in elements)
    
    networks[start] = result_tuple


step = 'AAA'
find  = 'ZZZ'
Nstep = 0

while find != step:
    left, right = networks[step]
    ins = Nstep % len(instruction)
    if instruction[ins] == 'L':
        step = left
    else:
        step = right
    Nstep += 1
    
print(Nstep)
    

