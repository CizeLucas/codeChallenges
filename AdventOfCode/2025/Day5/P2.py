validIds = []
results = []
maxVal = 0
answer = 0

def count_unique_numbers(intervals):
    # Sort by start
    intervals.sort()

    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    # Count numbers
    return sum(end - start + 1 for start, end in merged)


intervals = [(3, 5), (10, 13), (16, 20), (12, 18)]
print(count_unique_numbers(intervals))  # 14


def solve():
    global maxVal
    global answer
    try:
        with open("input.txt", "r") as file:
            for index, line in enumerate(file):
                inputLine = line.strip()
                if(len(inputLine) == 0):
                    continue
                
                if("-" in inputLine):
                    inputLine = list(map(int, inputLine.split('-')))
                    validIds.append([inputLine[0], inputLine[1]])
                    maxVal = max(maxVal, inputLine[1])
                    
            validIds.sort()
            for validId in validIds:
                start = validId[0]
                end = validId[1]
                if len(results) == 0 or start > results[-1][1]+1:
                    results.append([start,end])
                else:
                    results[-1][1] = max(results[-1][1], end)

            for start, end in results:
                answer += (end-start)+1

            print(results)
            print(answer)

    except FileNotFoundError:
        print("Error: The file 'input.txt' was not found.")

if __name__ == "__main__":
    solve()

"""
ANSWERS:
6333277814563 -> too low
6333277814569 -> too low
343143696885053 -> RIGHT ANSWER
"""