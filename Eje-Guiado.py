# Uso de funciones predefinidas
tipo = type("32")
print(tipo)

print(id(5))

print(str(10) + " es un string")
# Conversión de tipos y operaciones
print(int("42") + 10)
print(float(3) / 2)
# Uso del módulo math
import math
print(math.sqrt(25))
print(math.sin(math.pi / 2))
print(math.log10(1000))
# Definir y usar funciones propias
def nueva_linea():
    print()

def tres_lineas():
    nueva_linea()
    nueva_linea()
    nueva_linea()

print("Inicio")
tres_lineas()
print("Fin")
