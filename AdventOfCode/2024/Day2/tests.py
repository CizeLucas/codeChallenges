lineString = "20 21 24 25 27 29 27"

print(lineString.split())

vector = [int(num) for num in lineString.split()]

print(vector)

comparison_results = [[-1, 0], [0, 0], [1, 0]]
comparison_results[0][1] += 1 # First number is bigger

print(comparison_results)