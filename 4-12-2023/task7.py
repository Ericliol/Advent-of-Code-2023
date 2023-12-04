file = open('4-12-2023/input.txt', 'r')

Lines = file.readlines()
points = 0
for line in Lines:
    counter = 0
    winning_numbers = line.split("|")[0].split()[2:]
    holding_numbers = line.split("|")[1].split()
    for i in winning_numbers:
        if i in holding_numbers:
            counter += 1
    if counter > 0:
        points += pow(2, counter-1)
    
print(points)