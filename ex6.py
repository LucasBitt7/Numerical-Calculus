from numpy import array, zeros
import cmath

def gaussSeidel(matriz, vetor):
  m = len(matriz)
  n = len(matriz[0])
  x = zeros((m))
  comp = zeros((m))
  error = []
  TOL = 0.0002
  maxit = 5000
  i = 0
  while i < maxit:
    suma = 0
    i += 1
    for r in range(0, m):
      suma = 0
      for c in range(0, n):
        if (c != r):
          suma = suma+matriz[r, c] * x[c]
      x[r] = (vetor[r]-suma)/matriz[r, r]
      print(f'x[{r}]: {x[r]}')
    del error[:]
    for r in range(0, m):
      suma = 0
      for c in range(0, n):
        suma = suma+matriz[r, c] * x[c]
      comp[r] = suma
      dif = abs(comp[r]-vetor[r])
      error.append(dif)
      print(f'Erro em x[{r}] = {error[r]}') 
    if all(i <= TOL for i in error) is True:
      break
  print(f'Com {i} iterações.')
  for c in range(0, m):
    print(f'x[{c}]: {round(x[c],4)}')

matriz = array([
[3+3j,-1-1j,-1-1j],
[-1-1j,3+3j,-1-1j],
[-1-1j,-1-1j,3+3j]])

vetor = array([1,1,1])

gaussSeidel(matriz, vetor)