N, K = map(int, input().split())
A = list(map(int, input().split()))

B = []

for i in range(len(A)):
    fase = A[i]
    filtro = A[i]
    filterIndex = i

    while True:
        if(fase > filtro):
            B.append(filterIndex+1)
            break; 
        else:
            fase = fase + K
            filterIndex = filterIndex + 1
            if(filterIndex >= N):
                filterIndex = 0
            filtro = A[filterIndex]

print(str(B).replace('[','').replace(']','').replace(',',''))