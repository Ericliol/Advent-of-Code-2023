from django.forms import *
file = open('5-12-2023/test.txt', 'r')
Lines = file.readlines()
seeds = [int(item) for item in Lines[0].split()[1:]]
seeds_p2 = []
for i in  range(int(len(seeds)/2)):
    seeds_p2.append((seeds[2*i], seeds[2*i] + seeds[2*i+1]))


# for line in file:
#     if line == "/n":

def search_dest(sorce_dest:dict , sorce:list)->list:
    
    re = []
    find = False
    
    for i in sorce:
        find = False
        p, q = i
            
        for key_r in sorce_dest.keys():

            if i >= key_r[0] and i <= key_r[1]:
                print("find", i)
                
                dest = sorce_dest[key_r] + (i - key_r[0])
                re.append(dest)
                find = True
                break
        if not find:
            re.append(i)
    return re

temp_sorce_dest = {}
for line in Lines:
    line = line.strip()
    if line == "" :
        # print(temp_sorce_dest)
        seeds = search_dest(temp_sorce_dest, seeds)
        print(seeds)
        temp_sorce_dest= {}
        continue
    elif line[0].isdigit() :
        line_nums = [int(item) for item in line.split()]
        dest_range = line_nums[0]
        srouce_range = (line_nums[1], line_nums[1]+line_nums[2])
        temp_sorce_dest[srouce_range] = dest_range
        
seeds = search_dest(temp_sorce_dest, seeds)
print(seeds)
print(min(seeds))