matrix = []
foundPositions = []

debugMode = False

def count_rolls_adjacent(l, i):
    count = 0

    possiblePositions = [
                [l+1,i-1],  [l+1,i],    [l+1,i+1],
                [l,i-1],                 [l,i+1],
                [l-1,i-1],  [l-1,i],    [l-1,i+1],
                ]
    
    for position in possiblePositions:
        if(position[0]<len(matrix) and position[0]>=0 and position[1]<len(matrix[0]) and position[1]>=0): # is inbounds
            if(matrix[position[0]][position[1]] == '@'):
                count+=1

    return count

def solve():
    result = 0
    try:
        with open("input.txt", "r") as file:
            for index, line in enumerate(file):
                inputList = list(line.strip())
                matrix.append(inputList)
  
        for l, line in enumerate(matrix):
            for i, ch in enumerate(line):
                if ch != '@':
                    continue
                rolls_count = count_rolls_adjacent(l, i)
                if(rolls_count < 4):
                    result += 1
                    if(debugMode):
                        foundPositions.append([l,i])
                        print(f"[l, i] = [{l},{i}]: {rolls_count}")

        print(result)

        if(debugMode):
            for foundPosition in foundPositions:
                matrix[foundPosition[0]][foundPosition[1]] = 'X'
            for line in matrix:
                print("".join(line))

    except FileNotFoundError:
        print("Error: The file 'input.txt' was not found.")


if __name__ == "__main__":
    solve()