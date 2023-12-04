file = open('3-12-2023/input.txt', 'r')
grid = [list(line.strip()) for line in file if line.strip()]
adjacent_number_list=[]

def is_star(x, y):
    dot = grid[x][y] 
    return dot != '.' and not dot.isdigit()

def find_adjacent_numbers(x, y):
    return_numbers = []
    start_ends = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny].isdigit():
                    start = ny
                    while start > 0 and grid[nx][start - 1].isdigit():
                        start -= 1
                    end = ny
                    while end < len(grid[nx]) - 1 and grid[nx][end + 1].isdigit():
                        end += 1
                    startEnd = (start, end +1)
                    if (dx,startEnd) not in start_ends:
                        start_ends.append((dx,startEnd))
                        number = ''.join(grid[nx][start:end + 1])
                        return_numbers.append(int(number))
    return return_numbers


star_list = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        # print(x,y)
        if is_star(x,y):
            star_list.append((x,y))
print(star_list)

total = 0
for symbol in star_list:
    x , y = symbol
    returnList = find_adjacent_numbers(x, y)
    print(returnList)
    if len(returnList) ==2:
        total += returnList[0]*returnList[1]
print(total)