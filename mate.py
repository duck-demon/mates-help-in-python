import mate_main
import timeit
time = int(input("ingrese el tiempo de espera (00.000)  "))
print("1 - tres simples")
print("2 - multiplicacion y divicion")
print("3 - tablas de multiplicar")
print("4 - potencia al cuadrado")
print("5 - raiz cuadrada")
d1,d2,d3,aux = int,int,int,int
inus = int(input("op "))
if inus == 1: # regla de tres simples
    d1 = input("ingrese numero ")
    d2 = input("ingrese numero ")
    d3 = input("ingrese numero ")
    mm = mate_main.Main(d1,d2,d3)
    mm.rts()
elif inus == 2: # mul y div
    d1 = input("ingrese numero ")
    d2 = input("ingrese numero ")
    mm = mate_main.Main(d1,d2,d3)
    mm.md()
elif inus == 3: # tablas multiplicar
    d1 = input("tabla ")
    d2 = input("asta ")
    mm = mate_main.Main(d1,d2,d3)
    mm.tm()
elif inus == 4: # potencia al cuadrado
    d1 = input("ingrese numero ")
    mm = mate_main.Main(d1,d2,d3)
    mm.pc()
elif inus == 5: #raiz cuadrada
    d1 = input("ingrese numero ")
timeit.timeit('"-".join(str(n) for n in range(100))', number=time)
