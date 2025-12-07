import time

def benchmark(func):
    """Decorator to measure execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"\nExecution time: {elapsed_time:.6f} seconds")
        return result
    return wrapper


@benchmark
def solve():
    result = 0
    try:
        with open("input.txt", "r") as file:
            for index, line in enumerate(file):
                inputList = list(map(int, line.strip()))
                
                maxFound = 0
                for i in range(len(inputList)):
                    for j in range(i+1, len(inputList)):
                        curr = inputList[i]*10 + inputList[j]
                        if(curr > maxFound):
                            maxFound = curr
                #print(f"{maxFound} ({inputList})")
                result += maxFound

            print(result)

    except FileNotFoundError:
        print("Error: The file 'input.txt' was not found.")


if __name__ == "__main__":
    solve()