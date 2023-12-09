file = open('9-12-2023/input.txt', 'r')


lines = file.readlines()

def cal_nextval(nums:list)->int:
    current = nums.copy()
    lastVals = []
    lastVals.append(current[-1])
    
    
    while current.count(current[0]) != len(current):
      
        next = [current[i+1] - current[i] for i in range(len(current)-1)]
        lastVals.append(next[-1])
        current = next
        
    return sum(lastVals)

def cal_nextval_p2(nums:list)->int:
    current = nums.copy()
    FristVals = []
    FristVals.append(current[0])
    
    
    while (current.count(current[0]) != len(current)) or (current[0] != 0):
      
        next = [current[i+1] - current[i] for i in range(len(current)-1)]
        FristVals.append(next[0])
        
        current = next
        
    value = 0
    FristVals.reverse()
    for i in FristVals:
        value = i - value
    return value
        

total = 0 
for line in lines:
    numberList = [int(i) for i in line.strip().split()]
    total += cal_nextval_p2(numberList)
    
print(total)