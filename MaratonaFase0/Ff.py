from collections import defaultdict

def contar_quadruplas(N, A, queries):
    pair_sums = defaultdict(list)

    for i in range(N):
        for j in range(i + 1, N):
            s = A[i] + A[j]
            pair_sums[s].append((i, j))

    results = []

    for q in queries:
        count = 0
        seen = set()

        for s1 in pair_sums:
            s2 = q - s1
            if s2 in pair_sums:
                for i1, j1 in pair_sums[s1]:
                    for i2, j2 in pair_sums[s2]:
                        if len({i1, j1, i2, j2}) == 4:
                            quad = tuple(sorted([i1, j1, i2, j2]))
                            if quad not in seen:
                                seen.add(quad)
                                count += 1

        results.append(count)

    return results

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
queries = [int(input()) for _ in range(Q)]

for res in contar_quadruplas(N, A, queries):
    print(res)
