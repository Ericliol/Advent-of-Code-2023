file1 = open('7-12-2023/input.txt', 'r')

file1 = list(file1.readlines())

data = [(item.split()[0], int(item.split()[1]) )for item in file1]

import functools

sequence = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']

def order(list_inp: str):
    if 'J' not in list_inp:
        set_res = len(set(list_inp))
        if set_res == 1:
            return 1
        elif set_res == 2:
            for x in list_inp:
                if list_inp.count(x) == 4:
                    return 2 # Four of a kind
            return 3 # Full house
        elif set_res == 3:
            for x in list_inp:
                if list_inp.count(x) == 3:
                    return 4 # Three of a kind
            return 5 # Two pair 
        elif set_res == len(list_inp):
            return 7 # High card
        return 6
    jock_num = list_inp.count("J") 
    
    no_J = list(filter(lambda x: x if x != "J" else "", list_inp))
    if jock_num >= 4:
        return 1
    mostP = ""
    counter = 0
    for s in sequence:
        t = no_J.count(s)
        if t > counter:
            counter =t
            mostP = s
    mew =list_inp.replace("J", mostP)
    return order(mew)

# print(order('AAAAA'))
# print(order('AA8AA'))
# print(order('23332'))
# print(order('TTT98'))
# print(order('23432'))
# print(order('A23A4'))
# print(order('23456'))

def compare(a, b):
    a1, a2 = a
    b1, b2 = b
    Ta = order(a1)
    Tb = order(b1)
    if Ta == Tb:
        for i in range(len(a1)):
            if a1[i] != b1[i]:
                return -sequence.index(a1[i]) + sequence.index(b1[i])
        return 0 
    return Tb- Ta

# items = ["KK677", "KTJJT", "QQQJA", "AAAAA","32T3K","T55J5"]
sorted_items = sorted(data, key=functools.cmp_to_key(compare))

total = 0
count = 1
for i in sorted_items:
    total += count* i[1]
    count +=1
    

print(total)
