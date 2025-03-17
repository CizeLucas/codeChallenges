"""
-> TRIES:
1) 115859524991612357 -> too high
2) 184122457 -> correct!!!

"""

numbers = []
state = "BEGIN"
first_number = ""
second_number = ""

debbugMode = False

with open(r"C:\dev\codeChallenges\AdventOfCode\2024\Day3\input.txt", "r", encoding="utf-8") as file:
    content = file.read()

    for i in range(len(content)):
        first_number = ""
        second_number = ""
        if (content[i:i+3] == "mul" and state == "BEGIN"):
            state = "MUL_START"
            i += 3
            if(content[i] == '('):
                state = "PARAMETERS_START"
                i += 1
            else:
                state = "BEGIN"
                i += 1

        if(debbugMode):
            print(content[i:])
            print(state)

        if(state != "PARAMETERS_START"):
            state = "BEGIN"
        else:
            while(True):
                if(content[i].isdigit()):
                    state = "NUMBER_1"
                    first_number += content[i]
                    i += 1
                else:
                    break
        
        if(debbugMode):
            print(content[i:])
            print(state)

        if(content[i] == ',' and state == "NUMBER_1"):
            state = "COMMA"
            i += 1
        else:
            state = "BEGIN"

        if(debbugMode):
            print(content[i:])
            print(state)

        if(state != "COMMA"):
            state = "BEGIN"
        else:
            while(True):
                if(content[i].isdigit()):
                    state = "NUMBER_2"
                    second_number += content[i]
                    i += 1
                else:
                    break

        if(debbugMode):
            print(content[i:])
            print(state)

        if(content[i] == ')' and state == "NUMBER_2"):
            state = "MUL_END"
            i += 1
        else: 
            state = "BEGIN"
    
        if(state == "MUL_END"):
            numbers.append(int(first_number))
            numbers.append(int(second_number))
            print(f"found: {int(first_number)} * {int(second_number)}")
            first_number = ""
            second_number = ""

totalSum = 0
numbers_index = 0
while numbers_index < len(numbers):
    totalSum += numbers[numbers_index] * numbers[numbers_index+1]
    numbers_index += 2

print(len(numbers))
print(totalSum)