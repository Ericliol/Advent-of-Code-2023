import math
file1 = open('6-12-2023/input.txt', 'r')
total = 1
Line1 = file1.readline().strip().split()[1:]
Line2 = file1.readline().strip().split()[1:]
t_N_d = ("".join(Line1),"".join(Line2))



print(t_N_d)
def find_distance(time, dist):
    start = dist/time
    start = math.ceil(start) 
    i = 0
    while (start + i)*(time - start-i) < dist:
        i+=1
    return time- 2*(start+i) +1

        

time, dist = t_N_d
   
res = find_distance(int(time), int(dist))

print(res)   