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
                
                tens = max(inputList[:-1])
                # Does not consider the last number because it cannot form a pair
                ones = max(inputList[inputList.index(tens)+1:])
                # From the tens number found, now find the greatest one that can accompany it
                result += tens*10 + ones

            print(result)

    except FileNotFoundError:
        print("Error: The file 'input.txt' was not found.")

if __name__ == "__main__":
    solve()