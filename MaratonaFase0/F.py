from collections import defaultdict
from itertools import combinations

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
queries = [int(input()) for _ in range(Q)]

# 1. Construir dicionário com todas as somas de pares
pair_sums = defaultdict(list)

for i in range(N):
    for j in range(i + 1, N):
        s = A[i] + A[j]
        pair_sums[s].append((i, j))  # salva os índices para checar disjunção depois

# 2. Para cada qi, buscar quantas quádruplas somam qi
for q in queries:
    count = 0
    seen = set()  # evitar duplicação

    for s in pair_sums:
        complement = q - s
        if complement in pair_sums:
            list1 = pair_sums[s]
            list2 = pair_sums[complement]
            for i1, j1 in list1:
                for i2, j2 in list2:
                    # Verifica se os pares são disjuntos
                    if len({i1, j1, i2, j2}) == 4:
                        # Usar tupla ordenada para evitar contar permutações
                        quad = tuple(sorted([i1, j1, i2, j2]))
                        if quad not in seen:
                            seen.add(quad)
                            count += 1
    print(count)