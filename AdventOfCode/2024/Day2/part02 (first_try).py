safeLines = 0

def checkSafeRange(vector, anUnsafeLevelHasAlreadyOccurred):
    for index in range(len(vector)-1):
        if(not(1 <= abs(vector[index] - vector[index+1]) <= 3)):
            if(anUnsafeLevelHasAlreadyOccurred):
                anUnsafeLevelHasAlreadyOccurred = True
                return False
    return True

def checkVectorOrdering(vector, isAscendingOrder, anUnsafeLevelHasAlreadyOccurred):
    for i in range(len(vector) - 1):
        if(isAscendingOrder):
            if(not(vector[i] <= vector[i + 1])):
                if(anUnsafeLevelHasAlreadyOccurred):
                    anUnsafeLevelHasAlreadyOccurred = True
                    return False
        else:
            if(not(vector[i] >= vector[i + 1])):
                if(anUnsafeLevelHasAlreadyOccurred):
                    anUnsafeLevelHasAlreadyOccurred = True
                    return False
    return True

with open(r"C:\dev\codeChallenges\AdventOfCode\2024\Day2\input.txt", "r", encoding="utf-8") as file:
    for lineCount, lineString in enumerate(file, start=0):

        vector = [int(num) for num in lineString.split()] # converts the numbers of the line string into an vector

        vector_set = set(vector)
        if(len(vector_set) >= len(vector)-1): # Considers that at least one level could be disregarded

            anUnsafeLevelHasAlreadyOccurred = len(set(vector)) == len(vector)
            vector = list(vector_set)
            
            if(vector[0] > vector[1]): # if the vector is in descending order
                if (checkVectorOrdering(vector, False, anUnsafeLevelHasAlreadyOccurred)): # check if the whole vector in indeed in descending order
                    if(checkSafeRange(vector, anUnsafeLevelHasAlreadyOccurred)):
                        print(f"SAFE: {vector}")
                        safeLines += 1
                    else:
                        print(f"NOT SAFE (range not safe): {vector}")
                else:
                    print(f"NOT SAFE (not descending): {vector}")

            elif(vector[0] < vector[1]): # if the vector is in ascending order
                if (all(vector[i] <= vector[i + 1] for i in range(len(vector) - 1))): # check if the whole vector in indeed in ascending order
                    if(checkVectorOrdering(vector, True, anUnsafeLevelHasAlreadyOccurred)):
                        print(f"SAFE: {vector}")
                        safeLines += 1
                    else: 
                        print(f"NOT SAFE (range not safe): {vector}")
                else:
                    print(f"NOT SAFE (not ascending): {vector}")
        else:
            print(f"NOT SAFE (multiple repeated numbers): {vector}")

        if(lineCount == 5):
            break

print(safeLines)