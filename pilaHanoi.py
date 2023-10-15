
class nodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.debajo = None

        
class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0
    
    def apilar(self,valor):
        nodo = nodoPila(valor)
        nodo.debajo = self.cima #nodo. te permite acceder a elementos de la clase
        self.cima = nodo
        
    def desapilar(self):
        ret = self.cima.valor  #aqui self.cima = nodo (nodo.valor) accedemos al valor del nodo cima
        self.cima = nodo.valor
        