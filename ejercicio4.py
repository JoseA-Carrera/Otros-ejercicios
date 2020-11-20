'''
Ejercicio 4
Hacer un programa que pida 2 numeros y se de cuenta cual es par,
o si ambos los son.
'''
num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))

if num1%2==0 and num2%2==0:
    print("Ambos son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2==0:
    print(f"{num2} es par")
else:
    print("Ninguno es par")
