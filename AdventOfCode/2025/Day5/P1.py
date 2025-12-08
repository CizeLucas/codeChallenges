validIds = []
idsToCheck = []

def solve():
    result = 0
    try:
        with open("input.txt", "r") as file:
            for index, line in enumerate(file):
                inputLine = line.strip()
                if(len(inputLine) == 0):
                    continue
                
                if("-" in inputLine):
                    inputLine = list(map(int, inputLine.split('-')))
                    validIds.append([inputLine[0], inputLine[1]])
                else:
                    idsToCheck.append(int(inputLine))

            for idToCheck in idsToCheck:
                for validId in validIds:
                    if(validId[0] <= idToCheck <= validId[1]):
                        result+=1
                        #print(f"{idToCheck}: {validId[0]}, {validId[1]}")
                        break

            print(result)

    except FileNotFoundError:
        print("Error: The file 'input.txt' was not found.")

if __name__ == "__main__":
    solve()