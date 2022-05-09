import math as m
import numpy as np

Fmax = 50
a = 420
b = 696

def flechaFunction(C):
  return C*(m.cosh(250/C) - 1)-Fmax

def bisseccao(a,b):
  if(flechaFunction(a) * flechaFunction(b) >= 0):
      print("A condição f(a) * f(b) < 0 deve ser verdadeira!\n")
      return

  maxIteracoes = 50
  i = 0
  c = a
  tol = 0.000000001
   
  while((b - a) >= tol):  
        
      c = (a + b)/2

      if(flechaFunction(c) == 0.0): 
          break

      if(flechaFunction(c) * flechaFunction(a) < 0): 
          b = c
      else:
          a = c

      i += 1

  print("    x      = " ,c)
  print("   f(x)    = ", flechaFunction(c))
  print("   Error    = ", tol)
  print(" Iterações = ", i)

bisseccao(a, b)