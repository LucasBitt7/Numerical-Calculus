import math as m

def retificadorFunction(x,
      o=(m.atan(2*m.pi*abs(0+0.1j))),
      z=(2*m.pi*abs(0+0.1j)))->m.degrees:  
    return m.sin(x-o)+m.sin(o)*(m.exp(-x/z))

def bisseccao(x1, x2):
    TOL= 0.0001
    imax=50
    x = (x1 + x2)/2
    #print(x)
    if (retificadorFunction(x1) * retificadorFunction(x2) > 0):
        print("Not found")
    else:

      i = 0 
      ERRO = abs(retificadorFunction(x2) - retificadorFunction(x1)) 
      while (i < imax or ERRO > TOL): 
        x = (x1 + x2)/2  
        if (retificadorFunction(x) == 0):
            return [x, i] 
        if (retificadorFunction(x1) * retificadorFunction(x) < 0):
          
            x2 = x
            i += 1 
        else:
            x1 = x
        ERRO = abs(retificadorFunction(x2) - retificadorFunction(x1)) 
    return {"x": x*180/m.pi, "i": i}
 
result = bisseccao(abs(m.pi), abs(m.pi*2))
print('raiz aproximada =', result["x"])