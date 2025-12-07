"""
818181911112111
max(index - 11) ->  max(0 - 11)  /  max(1 - 11)  /  max(2 - 11)  /  max(3 - 11)

234234234234278
"""

result = 0
try:
    with open("input.txt", "r") as file:
        for index, line in enumerate(file):
            inputList = list(map(int, line.strip()))

            curr = 0
            for i in range(11):
                digit = max(inputList[:i-11])
                inputList = inputList[inputList.index(digit)+1:]
                curr = (curr*10)+digit
            
            curr = (curr*10) + max(inputList)
            result += curr


        print(result)

except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")