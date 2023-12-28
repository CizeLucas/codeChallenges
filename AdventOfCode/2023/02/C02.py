
keywords = [[0,1,2,3,4],["unknown","Game", "red", "green", "blue"]]


def get_spelled_keywords(string):
    for keyword_index in range(len(keywords[1])):
        if(keywords[1][keyword_index] in string):
            return keywords[0][keyword_index]
    return keywords[0][0]

def get_number(string, index):
    if(not string[index].isdigit):
        return -1
    
    first_num = int(string[index])

    if(string[index+1].isdigit):
        second_num = int(string[index+1])
        return first_num*10 + second_num
    else:
        return first_num

def get_cube_numbers(cube_line):
    game_num, red_num, green_num, blue_num = 0,0,0,0

    for index in range(len(cube_line)):
        index=4

        game_num=get_number(cube_line, index)

        str_temp=""

        if(cube_line[index]==" " or cube_line[index]=="," or cube_line[index]==":"):
            index+=1

        if(cube_line[index]==";"):
            index+=1

        while(cube_line[index]!="\n" and cube_line[index].isalpha):
            str_temp+=cube_line[index]
            index+=1
        #index+=-1
            
        if(cube_line[index]==" " or cube_line[index]=="," or cube_line[index]==":" or cube_line[index]=="\n"):
            index+=1

        if(cube_line[index]==";"):
            index+=1
        
        result = get_spelled_keywords(str_temp)

        if(result==0):
            print("unknown word")
        elif(result==2):
            red_num+=get_number(cube_line, index)
        elif(result==3):
            green_num+=get_number(cube_line, index)
        elif(result==4):
            blue_num+=get_number(cube_line, index)
        else:
            print("strange behavior...")

    return [game_num, red_num, green_num, blue_num]

directory = "C:\\dev\\codeChallenges\\AdventOfCode\\2023\\02\\"

file = open(directory+"input.txt", 'r')
#for i in range(10):
print(get_cube_numbers(file.readline()))