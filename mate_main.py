class Mate_b:
    def __init__(self,d1,d2,d3):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
class Rts (Mate_b): #regla de tres simples
    def rts(self):
        print("el resultado es ", self.d3*self.d2/self.d1)
class Md (Mate_b): #multiplicacion y deivicion
    def md(self):
        print("multiplicacion ", self.d1*self.d2)
        print("divicion ", self.d1/self.d2)
class Tm (Mate_b): #tablas de multiplicar
    def tm(self):
        aux = int
        for i in range(i,self.d2+1):  #error
            aux = d1*i
            print("{} X {} = {}".format(i,self.d1,aux))
class Pc (Mate_b): #potencia al cuadrado
    def pc(self):
        print("la potencia al cuadrado es ", self.d1*self.d1)
class Rc (Mate_b): #raiz cuadrada
    print("uwus")

class Main(Rts,Md,Tm,Pc,Rc):
    def __del__(self):
        print(" ") 

