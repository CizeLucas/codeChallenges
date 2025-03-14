# Tries:
# 1) ?? - ??
# 2) 684 - too high
# 3) 552 - too low
# 4) 588 - ??
# 5) 566 - CORRECT!!!

# Check if it is in a ascending or descending order
# Check if the absolute value of current number minus next number is between 1 and 3 (inclusive)

# 1)  7 6 4 2 1: Safe without removing any level.
# 2)  1 2 7 8 9: Unsafe regardless of which level is removed.
# 3)  9 7 6 2 1: Unsafe regardless of which level is removed.
# 4)  1 3 2 4 5: Safe by removing the second level, 3. 
# 5)  8 6 4 4 1: Safe by removing the third level, 4.
# 6)  1 3 6 7 9: Safe without removing any level.

# Input file has "m" lines with "n" numbers in each line

safeLines = 0

def checkVectorOrdering(vector, isAscendingOrder): # O(n) complexity
    if(isAscendingOrder):
        for i in range(len(vector) - 1):
            if(not(vector[i] <= vector[i + 1])):
                return False
    else:
        for i in range(len(vector) - 1):
            if(not(vector[i] >= vector[i + 1])):
                return False
    return True

def checkVectorIncrements(vector): # O(n) complexity
    for vectorIndex in range(len(vector)-1):
        if(not(1 <= abs(vector[vectorIndex] - vector[vectorIndex+1]) <= 3)):
            return False
    return True

with open(r"C:\dev\codeChallenges\AdventOfCode\2024\Day2\input.txt", "r", encoding="utf-8") as file:
    for lineCount, lineString in enumerate(file, start=0): 
        
        # O(m) complexity
        vector = [int(num) for num in lineString.split()] # converts the numbers of the line string into an vector
        hasAnyRemovedLevels = False
        isAscending = True

        # ascending:<  //  descending v[n] > v[n+1]
        
        comparison_results = [0, 0, 0]
        # comparison_results[0] indicates ascending order
        # comparison_results[1] indicates the numbers are equal
        # comparison_results[2] indicates descending order
        
        for index in range(len(vector)-1): # O(n) complexity
            if(vector[index] == vector[index+1]):
                comparison_results[1] += 1 # The numbers are equal
            elif (vector[index] > vector[index+1]):
                comparison_results[2] += 1 # Second number is bigger (indicating descending order)
            else: 
                comparison_results[0] += 1 # First number is bigger (indicating ascending order)       
        
        if(comparison_results[1] > 2):
            print(f"NOT SAFE (multiple repeated numbers): {vector}")
            continue # jumps this line because it is UNSAFE

        isAscending = comparison_results[0] > comparison_results[2]
        
        if(checkVectorOrdering(vector, isAscending) and checkVectorIncrements(vector)):
            # O(1) complexity
            safeLines += 1
            print(f"Safe Vector {vector}")
        else:
            for index in range(len(vector)):
                # O(n) complexity
                test_vector = vector[:index] + vector[(index+1):]
                if(checkVectorOrdering(test_vector, isAscending) and checkVectorIncrements(test_vector)):
                    safeLines += 1
                    print(f"Safe Vector {vector} by removing {vector[index]}")
                    break # jumps the iterations over this vector (line) because it is safe

        
    print(f"FINAL Safe Line Count = {safeLines}")