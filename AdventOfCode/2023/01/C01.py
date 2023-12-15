#  --- Day 1: Trebuchet?! ---

def get_calibration_numbers(string):
    # first_number -> stores the first number it finds in the line
    # second_number -> will store all the other numbers found while iterating over the line 
    firstNumber = -1
    secondNumber = -1
    for i in range(len(string)):
        if string[i].isdigit():
            if firstNumber!=(-1):
                secondNumber = int(string[i])
            else:
                firstNumber = int(string[i])

            if secondNumber==(-1):
                secondNumber = firstNumber

    finalResult = firstNumber*10 + secondNumber

    print(f"{string} -> {finalResult}") 

    return finalResult


directory = "C:\\dev\\codeChallenges\\AdventOfCode\\2023\\01\\"
"""
file = open(directory+'input.txt', "r")

sum_of_calib_values=0
counter = 0

for line in file:
    print(f"{counter}) ")
    sum_of_calib_values += get_calibration_numbers(file.readline()[:-1])
    counter+=1
    # string[:-1] excludes the last character of the string (excludes '\n')
    

print(f"The sum of all the calibration values is: {sum_of_calib_values}")

file.close()
"""

with open(directory+"input.txt", 'r') as file:
    counter=1
    sum_of_calib_values=0

    for i in range(1000):
        print(f"{counter}) ")
        sum_of_calib_values += get_calibration_numbers((file.readline()[:-1]))
        counter+=1
        # string[:-1] excludes the last character of the string (excludes '\n')

print(f"The sum of all the calibration values is: {sum_of_calib_values}")
#SPOILER: the answer is 54304