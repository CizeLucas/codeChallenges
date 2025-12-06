position = 50
result = 0

try:
    with open("input.txt", "r") as file:
        for index, line in enumerate(file):
            inputLine = line.strip()
            print(inputLine)

            lastPosition = position

            isLeftRotation = (inputLine[0] == 'L')

            fullRotations = (abs(int(inputLine[1:])) // 100)
            print(f"full rotations = {fullRotations}")
            result += fullRotations

            if(isLeftRotation):
                position -= (int(inputLine[1:]) % 100)
            else:
                position += (int(inputLine[1:]) % 100)

            position = position % 100

            if(isLeftRotation and lastPosition < position):
                result += 1
                print("PASSED THROUGH ZERO BY ROTATING LEFT")
            elif(not isLeftRotation and lastPosition > position):
                result += 1
                print("PASSED THROUGH ZERO BY ROTATING RIGHT")
            
            print(f'position {position} // result {result}\n')
        
        print(result)

except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")