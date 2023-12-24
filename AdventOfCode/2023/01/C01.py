directory = "C:\\dev\\codeChallenges\\AdventOfCode\\2023\\01\\"
numbers = (["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], [1,2,3,4,5,6,7,8,9])

consider_spelled_numbers = False 
#True for considering the spelled numbers of the calibration codes
#False for only considering the numerical characters of the calibration codes

#Function returns -1 if a spelled number is not found or the numerical value of the number if it is found
def get_spelled_numbers(string):
    if(len(string)<3):#if condition to not execute the entire function if the string input has less than three characters
        return -1
    for index in range(len(numbers[0])):
        if(string.find(numbers[0][index])!=-1):
            return numbers[1][index]
    return -1 #spelled number not found

def get_calibration_numbers(string): #gets the string (whole line of the input.txt) and decipher the calibration values
    first_num = -1
    second_num = -1
    
    for i in range(len(string)):
        if(string[i].isdigit()): #if the character is a number, save it
            if(first_num==-1): #if condition makes sure that the first_number variable is only assingned one time
                first_num=int(string[i])
            else:
                second_num=int(string[i])

        elif(string[i].isalpha() and consider_spelled_numbers): #reads the characters until a spelled number is found or it finds a non alphabetical character or is the end of the string
            strTemp=""
            while(i<len(string) and string[i].isalpha()):
                strTemp+= string[i]
                spelled_num = get_spelled_numbers(strTemp)
                if(spelled_num!=-1):
                    if(first_num==-1):
                        first_num=spelled_num
                    else:
                        second_num=spelled_num
                    break
                if(i<len(string)-1 and string[i+1].isalpha()):
                    i+=1
                else:
                    break
                
        else:
            if(consider_spelled_numbers):
                print("unknown character")

    if(second_num==-1): #if only one number (spelled or not) is found, the second_num will recive the value of first_num
        second_num = first_num

    return first_num*10 + second_num


"""
file = open(directory+"input.txt", 'r')
for i in range(10):
    print(get_calibration_numbers(file.readline()))
"""

with open(directory+"input.txt", 'r') as file:
    counter=1
    line_text=""
    calib_values=0
    sum_of_calib_values=0
    
    for i in range(1000):
        line_text=file.readline()
        calib_values = get_calibration_numbers(line_text)
        sum_of_calib_values += calib_values
        print(f"{line_text[:-1]}) {calib_values} ")
        counter+=1

print(f"The sum of all the calibration values is: {sum_of_calib_values}")
#SPOILER: the first right answer is 54304 (consider_spelled_numbers = False)
#SPOILER: the second right answer is 54418 (consider_spelled_numbers = True)