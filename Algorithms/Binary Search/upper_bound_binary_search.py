# UPPER BOUND de X: A menor posição em que aparece um número maior que X no nosso vetor
# Busca a menor posição onde aparece numeros ESTRITAMENTE maiores que o de alvo

vect = [1, 2, 2, 2, 2, 4, 5, 5, 6, 6, 7, 7, 7, 9, 10, 12]

print(vect)

target = int(input("Enter the target value to which the UPPER BOUND index will be calculated: "))

n = len(vect)
l, r = 0, n - 1
mid = 0
upperBoundIndex = -1

while(l <= r):
    mid = int((l + r) / 2)

    print(f"Janela de busca: {vect[l : r+1]}")
    print(f"Pesquisando no index {mid} (Valor {vect[mid]}).")
    print(f"Ponteiros l = {l} e r = {r}")
    if(vect[mid] > target):
        print(f"\t Valor MAIOR que target, ajustando o ponteiro direito r de {r} para {mid-1}")
        upperBoundIndex = mid
        r = mid-1
    else: # vect[mid] <= target
        print(f"\t Valor MENOR ou IGUAL que target, ajustando o ponteiro esquerdo l de {l} para {mid+1}")
        l = mid+1
        

print('\n')
if(upperBoundIndex == -1):
    print("UPPER BOUND NOT FOUND")
else:
    print(f"The UPPER bound of the value {target} is {vect[upperBoundIndex]}, found at index {upperBoundIndex} of main array")
