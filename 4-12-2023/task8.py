file = open('4-12-2023/input.txt', 'r')

Lines = file.readlines()
points = 0
card_instance = {}
for line in Lines:
    card_number = int(line.split("|")[0].split()[1][:-1])
    card_instance[card_number] = 1

for line in Lines:
    counter = 0
    card_number = int(line.split("|")[0].split()[1][:-1])
    winning_numbers = line.split("|")[0].split()[2:]
    holding_numbers = line.split("|")[1].split()
    current_copy = card_instance[card_number]
    for i in winning_numbers:
        if i in holding_numbers:
            counter += 1
    for k in range(counter):
        if card_number+k < len(card_instance):
            card_instance[card_number+k+1] += current_copy
    


    
print(card_instance)
print(sum(card_instance.values()))