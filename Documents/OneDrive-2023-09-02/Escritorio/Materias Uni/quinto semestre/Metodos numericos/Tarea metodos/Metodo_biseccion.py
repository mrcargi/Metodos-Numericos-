#APLICACION DEL METODO DE BISECCION 

import sympy as sp
from prettytable  import PrettyTable


x= sp.Symbol('x')
fx = x**3-6*x**2+9*x-3.75
print(fx)        #Imprimo la funcion


a = 0
b = 1



def biseccion(a,b,error = 0.0001,max_iter= 100):
    if fx.subs(x,a) == 0:
        return a 
    elif fx.subs(x,b) == 0:
        return b
    
    
    if fx.subs(x,a)*fx.subs(x,b) > 0:
        return None
    m_previo = None
    tabla = PrettyTable()
    tabla.field_names=["#Iteracion","a","b","m","f(a)","f(b)","f(m)","Error%"]
    tabla.title = f"METODO DE BISECCION Para la funcion : {fx} "
    
    for i in range(max_iter):
        
        m = (a+b)/2 
 
        
        if fx.subs(x,m) == 0 or (b-a)/2 < error:
            break
        
        
        if fx.subs(x,m) * fx.subs(x,a)< 0:
            b = m
        else :
            a = m
        
        if m_previo is not None:
            errorc = (((m) - m_previo)/m) *100
        else:
            errorc = "NA"
            
        
            
        tabla.add_row([i+1,a,b,m,fx.subs(x,a),fx.subs(x,b),fx.subs(x,m),errorc])
            
        # if m_previo is not None:
        #     errorc = (((m) - m_previo)/m) *100
        #     print(f"Iteracion {i + i}: a = {a}, b = {b} , error = {errorc} % , m = {m}")
        # else:
        #     print (f"Iteracion {i + i}: a = {a}, b = {b} , error = NA % , m = {m}")   
        
        m_previo = m
        
    print("Numero maximo de iteraciones alcanzado")
    print(tabla)
    

raiz = biseccion(a,b)
 

