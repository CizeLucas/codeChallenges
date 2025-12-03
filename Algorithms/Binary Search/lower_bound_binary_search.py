# LOWER BOUND de X: A menor posição que aparece um número maior ou igual que X no nosso vetor
# Busca a menor posicao onde aparecem numeros maiores ou iguais ao alvo

vect = [1, 2, 2, 2, 2, 4, 5, 5, 6, 6, 7, 7, 7, 9, 10, 12]

print(vect)

target = int(input("Enter the target value to which the LOWER BOUND index will be calculated: "))

n = len(vect)
l, r = 0, n - 1
mid = 0
lowerBoundIndex = -1

while(l <= r):
    mid = int((l + r) / 2)

    print(f"Janela de busca: {vect[l : r+1]}")
    print(f"Pesquisando no index {mid} (Valor {vect[mid]}).")
    print(f"Ponteiros l = {l} e r = {r}")
    if(vect[mid] >= target):
        print(f"\t Valor MAIOR ou IGUAL que target, ajustando o ponteiro direito r de {r} para {mid-1}")
        lowerBoundIndex = mid
        r = mid-1
    else: # vect[mid] < target
        print(f"\t Valor MENOR que target, ajustando o ponteiro esquerdo l de {l} para {mid+1}")
        l = mid+1
        

print('\n')
if(lowerBoundIndex == -1):
    print("LOWER BOUND NOT FOUND")
else:
    print(f"The LOWER bound of the value {target} is {vect[lowerBoundIndex]}, found at index {lowerBoundIndex} of main array")