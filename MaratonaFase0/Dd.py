N = int(input())
S = input().strip()
T = input().strip()

qubit_superposition_s = S.count('*')
qubit_superposition_t = T.count('*')

# Evita divisão por zero
if qubit_superposition_s != 0:
    resultado = 1 - (qubit_superposition_t / qubit_superposition_s)
    print(f"{resultado:.2f}")
