'''
*Ejercicio 2*
 crear un programa para ingresar el radio de un circulo y se reporte
 su area y la longitud de la circuferencia
 formulas:
 area = pi * radio al cuadrado
 longitud de circuferencia = 2 * pi * radio
 para decidir la cantidad de decimales se hace esto {"variable":.2f}
'''
import math

radio = float(input("radio = "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"El area es: {area:.2f}")
print(f"La longitud de la circuferencia es: {longitud:.2f}")
