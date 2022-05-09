from math import pi, exp
import numpy as np

x = np.asarray([2,1])
i = 0
imax = 5
error = 0.001
while True:
  x1 = 31.9824*10**(-9)*(-1 + exp(x[1]/0.00462))-x[0]
  x2 = ((x[1])/(1/31.9824 * 10 ** (-9))-x[0])

  F = np.array([x1,x2])
  J = np.array([[(31.9824 * 10 ** (-9))*(-1 + exp((x[1])/0.004627276))-
(x[0])],[(x[1])/(1/(31.9824 * 10 ** (-9))-(x[0]))]]) 
  
  dx = np.linalg.lstsq(J,F,rcond=None)[0]
  x = x - dx
 
  i += 1
  ea = max(abs( np.divide( dx , x )))
  if i  >= imax or ea <= error :
    break
  print(f'Com {i} iterações: \n x = \n { x }' )