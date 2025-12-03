X = int(input())

Y = X

if(Y%2 == 0):
    Y -= 1

while(Y >= 1):
    y_bin = str(bin(Y)[2:])
    if(y_bin == y_bin[::-1]):
        break

    Y -= 2



print(Y)