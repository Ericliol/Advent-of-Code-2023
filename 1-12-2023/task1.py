


file1 = open('1-12-2023/input.txt', 'r')
total = 0
Lines = file1.readlines()
for line in Lines:
    print("{}".format( line.strip()))
    temp =  line.strip()
    res = [int(i) for i in temp if i.isdigit()]
    total += res[0]*10+res[-1]
    # print(res)
print(total)
