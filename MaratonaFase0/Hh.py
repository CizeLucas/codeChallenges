X = int(input())

Y = X

y_bin = str(bin(Y)[2:])

half_length_int = len(y_bin) // 2

if(len(y_bin)% 2 == 0):
    first_half = y_bin[:half_length_int]
    second_half = y_bin[half_length_int:]
    if(int(first_half, 2) > int(second_half, 2)):
        #first half is greater
        
        else:
        #second half is greater
    else:
