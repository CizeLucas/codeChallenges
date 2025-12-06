position = 50
result = 0
increments = 0

try:
    with open("input.txt", "r") as file:
        for index, line in enumerate(file):
            inputLine = line.strip()

            isLeftRotation = (inputLine[0] == 'L')

            turns = int(inputLine[1:])
            print(f"{"LEFT" if isLeftRotation else "RIGHT"} by {turns}")

            if(isLeftRotation):
                increments = -1
            else:
                increments = 1
            
            for i in range(turns):
                position += increments
                
                position = position % 100

                if position == 0:
                    result += 1

        print(result)

except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")