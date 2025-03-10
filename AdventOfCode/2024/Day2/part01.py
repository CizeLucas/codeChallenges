safeLines = 0

def checkSafeRange(vector):
    for index in range(len(vector)-1):
        if(not(1 <= abs(vector[index] - vector[index+1]) <= 3)):
            return False
    return True

with open(r"C:\dev\codeChallenges\AdventOfCode\2024\Day2\input.txt", "r", encoding="utf-8") as file:
    for lineCount, lineString in enumerate(file, start=0):

        vector = [int(num) for num in lineString.split()] # converts the numbers of the line string into an vector
        print(vector)
        if(len(set(vector)) == len(vector)):
            if(vector[0] > vector[1]): # if the vector is in descending order
                if (all(vector[i] >= vector[i + 1] for i in range(len(vector) - 1))): # check if the whole vector in indeed in descending order
                    if(checkSafeRange(vector)):
                        print(f"SAFE: {vector}")
                    safeLines += (1 if checkSafeRange(vector) else 0)
                else:
                    print("false")

            elif(vector[0] < vector[1]): # if the vector is in ascending order
                if (all(vector[i] <= vector[i + 1] for i in range(len(vector) - 1))): # check if the whole vector in indeed in ascending order
                    if(checkSafeRange(vector)):
                        print(f"SAFE: {vector}")
                    safeLines += (1 if checkSafeRange(vector) else 0)
                else:
                    print("false")
        

print(safeLines)