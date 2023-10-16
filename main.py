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
    if n == 1:
        print("D1 from ",pila1,"to",pila3)
        tablero[pila3].apilar(tablero[pila1].desapilar())
        return
    resolver(n-1, tablero, pila1, pila3, pila2)
    print(f"D{n} from {pila1} to {pila3}")
    tablero[pila3].apilar(tablero[pila1].desapilar())
    resolver(n-1, tablero, pila2, pila1, pila3)

discos = 3
tablero = getTablero(discos)

resolver(discos, tablero, 0, 1, 2)
