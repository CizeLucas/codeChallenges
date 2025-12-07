bank = [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]

for index in range(11):
    temp = bank[:index - 11]
    digit = max(temp)
    bank = bank[bank.index(digit)+1:]
    print(temp)
    print(digit)
    print(bank)
    #[8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]
    #doing [:-11] removes: 8,1,9,1,1,1,1,2,1,1,1
    #ending up with only: [8,1,8,1]