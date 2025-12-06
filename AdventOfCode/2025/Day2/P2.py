from collections import Counter

def get_repeating_prefix(s):
    # (s + s) creates "1122112211221122"
    # .find(s, 1) looks for "11221122" starting from index 1
    
    # It will find it at index 4 (which is the length of "1122")
    length = (s + s).find(s, 1)
    
    # If length is not -1 and strictly less than len(s), we found a period
    if length != -1 and length < len(s):
        return s[:length]
    return None


with open("input.txt", "r") as arquivo:
    input = arquivo.readline()
    ranges = input.split(',')
    result = 0
    invalidResults = []

    numberRanges = []
    for range in ranges:
        numberRanges.append(range.split('-'))
    
    for index, numberRange in enumerate(numberRanges):
        number = int(numberRange[0])
        while(number <= int(numberRange[1])):
            numberStr = str(number)

            sb = get_repeating_prefix(numberStr)
            if(sb == None):
                number+=1
                continue

            sbStr = str(sb)

            if len(numberStr) % len(sbStr) != 0:
                number+=1
                continue

            fullSb = sbStr * (len(numberStr) // len(sbStr))

            if(numberStr != fullSb):
                number+=1
                continue

            print(f"INVALID: {number}")
            result += number
            invalidResults.append(number)
        
            number+=1

    print(result)
    print(invalidResults)