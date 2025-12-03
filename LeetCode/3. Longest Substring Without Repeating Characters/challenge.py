# Substring mais longa SEM caracteres repetidos

input = "abcabcbb"
inputSet = set(input)
print(inputSet.__str__())

print(input.__contains__(inputSet.__str__()))


for i in range(len(input)):
    print(input[i])


def str_way(input: str):
    substring = ""
    for i in range(len(input)):
        substring += input[i]

    return substring