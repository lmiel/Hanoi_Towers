from pilaHanoi import *

def getTablero(n):
    tablero = []
    tablero.append(Pila())
    tablero.append(Pila())
    tablero.append(Pila())
    for n in range(n,0,-1):
        tablero[0].apilar(n)
    return tablero

def resolver(n,tablero,pila1,pila2,pila3):
    if n = 1:
        print("D1 from ",pila1,"to",pila3)
    
    

tablero = getTablero(4)