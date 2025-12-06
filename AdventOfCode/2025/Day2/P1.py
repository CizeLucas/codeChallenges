with open("input.txt", "r") as arquivo:
    input = arquivo.readline()
    ranges = input.split(',')
    result = 0

    numberRanges = []
    for range in ranges:
        numberRanges.append(range.split('-'))
    
    for numberRange in numberRanges:
        number = int(numberRange[0])
        while(number <= int(numberRange[1])):
            numberStr = str(number)

            if len(numberStr)%2 == 0:
                if (numberStr[: len(numberStr)//2] == numberStr[len(numberStr)//2 :]):
                    print(number)
                    result += number

            number+=1

    print(result)