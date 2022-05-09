import numpy as np 


def decomposicaoLU(A, b):
    m = len(A)
    y = np.zeros(m)
    x = np.zeros(m)
    U = A
    L = np.zeros([m, m])
    for k in range(0, m):
        for r in range(0, m):
            if (k == r):
                L[k, r] = 1
            if (k < r):
                factor = (A[r, k]/A[k, k])
                L[r, k] = factor
                for c in range(0, m):
                    U[r, c] = A[r, c] - (factor * A[k, c])
    A = np.zeros([m, m])
    for r in range(0, m):
        for c in range(0, m):
            for k in range(0, m):
                A[r, c] += (L[r, k] * U[k, c])

    print('A',A)
    print('L', L)
    print('U', U)
    # RESOLUÇÃO DAS EQUAÇÕES MATRICIAIS
    ###################################
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    ###################################
    f = 'SOLUÇÃO DO SISTEMA'
    print('-'*(len(f)+32))
    print(f'{f:^50}')
    print('-'*(len(f)+32))
    print('x =',x)
    print('Onde: ')
    for c in range(0, len(x)):
        print(f'\t x[{c}] = {x[c]} \n')

# Uso do método
A = np.array([[10,20],
              [20,10]])
b = np.transpose([100,100])

decomposicaoLU(A, b)