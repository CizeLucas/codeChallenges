position = 50
result = 0

try:
    with open("input.txt", "r") as file:
        for index, line in enumerate(file):
            inputLine = line.strip()
            isLeftRotation = (inputLine[0] == 'L')
            
            oldPosition = position

            fullRotations = (abs(int(inputLine[1:])) // 100)
            print(f"full rotarions = {fullRotations}")
            result += fullRotations
            if(isLeftRotation):
                position -= (int(inputLine[1:]) - (99*fullRotations))
            else:
                position += (int(inputLine[1:]) - (99*fullRotations))

            if(position > 99):
                position = position % 100
            elif(position < 0):
                position = (100-(position)*(-1) % 100) % 100

            if(isLeftRotation and oldPosition < position):
                result += 1
                print("FOUND")
            elif(not isLeftRotation and oldPosition > position):
                result += 1
                print("FOUND")
            
            print(f'position {position} // result {result}')
        
        print(result)

except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")