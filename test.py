# from collections import Counter

# dict = {}

# dict[0] = 1
# dict[1] = 1

# print(dict.items())

# print(dict)

# counterDict = Counter("carrace")

# print(counterDict)
# print(type(counterDict))

# str = "Python"

# print(sorted(str))
# print(''.join(sorted(str)))

strs =["eat","tea","tan","ate","nat","bat"]

# dic = {}
# for str in strs:
#     print(f'Processing string: {str}')
#     key = ''.join(sorted(str))
#     if key not in dic:
#         print(f'key {key} NOT exists')
#         dic[key] = [str]
#         print(f'dic[{key}] = {[str]}')
#     else:
#         print(f'key {key} exists')
#         dic[key].append(str)
#         print(f'dic[{key}].append({str})')

# print(dic)

dic = {}
for str in strs:
    key = ''.join(sorted(str))
    if key not in dic:
        dic[key] = [str]
    else:
        dic[key].append(str)
    
answer = []
for key, value in dic.items():
    answer.append(value)

print(answer)