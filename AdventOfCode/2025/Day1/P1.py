position = 50
result = 0

try:
    with open("input.txt", "r") as file:
        for index, line in enumerate(file):
            inputLine = line.strip()
            isLeftRotation = (inputLine[0] == 'L')

            rest = int(inputLine[1:])

            result += rest // 100
            rest = rest % 100

            oldPosition = position

            if(isLeftRotation):
                position -= rest
            else:
                position += rest

            if(position > 99):
                position = position % 100
            elif(position < 0):
                position = (100-(position)*(-1) % 100) % 100

            if(isLeftRotation and oldPosition < position):
                result += 1
            elif(not isLeftRotation and oldPosition > position):
                result += 1
            
            print(f'position {position} // result {result}')
        
        print(result)

except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")

    