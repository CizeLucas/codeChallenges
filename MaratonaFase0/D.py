N, S, T = map(str, input().split('\n'))

qubit_superposition_s = S.count('*')

qubit_superposition_t = T.count('*')

print( 1 - (qubit_superposition_t / qubit_superposition_s)+'\n' )