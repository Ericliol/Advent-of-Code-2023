words = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7,"eight":8,"nine":9}


def get_number(line:str) -> int:
    number_list = []
    tempword = ""
    for char in line:
        if char.isdigit():
            number_list.append(int(char))
            tempword = ""
        else:
            tempword += char
            for key in words.keys():
                if key in tempword:
                    number_list.append(words[key])
                    tempword = ""

    return number_list[0]

def get_l_number(line:str) -> int:
    number_list = []
    tempword = ""
    count = len(line)-1
    while count >= 0:
        char = line[count]
        count = count - 1
        if char.isdigit():
            number_list.append(int(char))
            tempword = ""
        else:
            tempword = char + tempword
            for key in words.keys():
                if key in tempword:
                    number_list.append(words[key])
                    tempword = ""

    return number_list[0]

res = get_number("twone")
print(res)
res = get_l_number("twone")
print(res)

file1 = open('input.txt', 'r')
total = 0
Lines = file1.readlines()



for line in Lines:
    # print("{}".format( line.strip()))
    temp =  line.strip()
   
    num1 = get_number(temp)
    num2 = get_l_number(temp)
    total += 10*num1+ num2
    # print(res)
print(total)