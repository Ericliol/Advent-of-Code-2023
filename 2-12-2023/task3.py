file1 = open('2-12-2023/input.txt', 'r')

target = {"red":12, "green":13, "blue":14}

def check_strings(game:[str])->bool:
    for set in game:
        parts = set.split(", ")
        for part in parts:
            part_split = part.split()
            color = part_split[1]
            number = part_split[0]
            if target[color] < int(number):
                return False
    return True


counter = 0
res = 0
Lines = file1.readlines()
for line in Lines:
    # print("{}".format( line.strip()))
    counter = counter + 1
    temp =  line.strip()
    
    counterStr = "Game " + str(counter) + ": "
    temp = temp.replace(counterStr,"").split(";")
    if check_strings(temp):
        res += counter
    print(temp)

print(res)

