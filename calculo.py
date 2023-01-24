import random
import math

def moneda():
    
    resultado = 0
    mone = ""

    resultado = random.randint(1,2)

    if resultado == 1:
        mone = "Cara"
    else: 
        mone = "Cruz"

    mensaje = mone

    mensaje = str(mensaje)

    return mensaje

def d3Lados():
    cara = 0
    
    resultado = 0

    cara= random.randint(1,6)
    if cara > 3:
        resultado= math.ceil(cara/2)
    else:
        resultado = cara
    
    resultado = str(resultado)
    cara= str(cara)
    
    mensaje = "cara " + cara + "\n Resultado " + resultado

    return mensaje



def d4Lados():
    
    suma = 0
    lista1=[1,2,3]
    lista2=[1,2,4]
    lista3=[1,3,4]
    lista4=[2,3,4]


    suma = random.randint(6,9)

    if suma == 6:
        cara = lista1
    elif suma == 7:
        cara = lista2
    elif suma == 8:
        cara = lista3
    else:
        cara = lista4

    suma = str(suma)
    cara = str(cara)

    mensaje = "cara: " + cara + "\n Total: " + suma

    return mensaje

def d6Lados():
    
    resultado = 0

    resultado = random.randint(1,6)
    
    mensaje = resultado

    mensaje = str(mensaje)

    return mensaje

def d8Lados():
    
    resultado = 0

    resultado = random.randint(1,8)
    
    mensaje = resultado

    mensaje = str(mensaje)

    return mensaje

def d10aLados():
    
    resultado = 0

    resultado = random.randint(0,9)
    
    mensaje = resultado

    mensaje = str(mensaje)

    return mensaje

def d10bLados():
    
    resultado = 0

    resultado = random.randint(1,10)

    mensaje = resultado

    mensaje = str(mensaje)

    return mensaje

def d12Lados():
    
    resultado = 0

    resultado = random.randint(1,12)
    
    mensaje = resultado

    mensaje = str(mensaje)

    return mensaje

def d20Lados():
    
    resultado = 0

    resultado = random.randint(1,20)
    
    mensaje = resultado

    mensaje = str(mensaje)

    return mensaje


def d30Lados():
    
    resultado = 0

    resultado = random.randint(1,30)
    
    mensaje = resultado

    mensaje = str(mensaje)

    return mensaje

def d100Lados():
    
    resultado = 0

    resultado = random.randint(1,100)
    
    mensaje = resultado

    mensaje = str(mensaje)

    return mensaje