#  --- Day 1: Trebuchet?! ---

numbers = (['o', 't', 'f', 's', 'e', 'n'], ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], [1,2,3,4,5,6,7,8,9])

def get_calibration_numbers(string):
    # first_number -> stores the first number it finds in the line
    # second_number -> will store all the other numbers found while iterating over the line 
    firstNumber = -1
    secondNumber = -1
    spelled_number = -1
    for i in range(len(string)-1):
        if string[i].isdigit():
            #print(int(string[i]))
            if firstNumber!=-1:
                secondNumber = int(string[i])
            else:
                firstNumber = int(string[i])
            #print(f"firstNumber: {firstNumber} // secondNumber:{secondNumber}")
        else:
            if string[i] in numbers[0]:
                spelled_number = get_spelled_numbers(string[i:])

            if spelled_number!=-1:
                if firstNumber!=-1:
                    secondNumber = spelled_number
                else:
                    firstNumber = spelled_number
        spelled_number = -1

    if(secondNumber==(-1)):
        secondNumber = firstNumber

    finalResult = firstNumber*10 + secondNumber

    #print(f"{string} -> {finalResult}") 

    return finalResult

# o, t, f, s, e, n
def get_spelled_numbers(string):
    for index in range(len(numbers[1])):
        if(string[:3] in numbers[1][index]):
            return numbers[2][index]
        
    for index in range(len(numbers[1])):
        if(string[:4] in numbers[1][index]):
            return numbers[2][index]
        
    for index in range(len(numbers[1])):
        if(string[:5] in numbers[1][index]):
            return numbers[2][index]
        
    return -1


directory = "C:\\dev\\codeChallenges\\AdventOfCode\\2023\\01\\"
"""
file = open(directory+"input.txt", 'r')
for i in range(10):
    #file.readline()
    print(get_calibration_numbers(file.readline()))

"""

with open(directory+"input.txt", 'r') as file:
    counter=1
    sum_of_calib_values=0

    for i in range(1000):
        print(f"{counter}) ")
        sum_of_calib_values += get_calibration_numbers((file.readline()))
        counter+=1

print(f"The sum of all the calibration values is: {sum_of_calib_values}")
#SPOILER: the first answer is 54304
