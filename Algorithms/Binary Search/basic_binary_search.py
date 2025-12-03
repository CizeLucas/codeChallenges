vect = []

for i in range(1, 11):
    vect.append(i)

print(vect)

target = int(input("Enter the target value to search for: "))
targetFound = False

n = len(vect)
l, r = 0, n - 1
mid = 0

while(l <= r):
    mid = int((l + r) / 2)

    print(f"Janela de busca: {vect[l : r+1]}")
    print(f"Pesquisando no index {mid} (Valor {vect[mid]}).")

    if(vect[mid] == target):
        targetFound = True
        break
    elif(vect[mid] < target):
        print(f"\t Valor MENOR que target, ajustando o ponteiro esquerdo l de {l} para {mid+1}")
        l = mid+1
    else: # vect[mid] > target
        print(f"\t Valor MAIOR que target, ajustando o ponteiro direito r de {r} para {mid-1}")
        r = mid-1

if targetFound: 
    print(f"Value {target} found at index {mid} of main array")
else:
    print("Value not found")