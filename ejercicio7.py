'''
Ejercicio 7
crear un programa que simule el funcionamiento de una calculadora
que puede realizar las cuatro operaciones aritmeticas basicas
(suma, resta, multiplicacion y division). El usuario debe especificar
la opeeracion con el primer caracter del nombre de la operacion.
'''
print("\nSuma(s), Resta(r), Multiplicacion(m), Division(d) ")

sep = '-' * 15

num1 = float(input("\nDigite un numero: "))
num2 = float(input("Digite otro numero: "))

operacion = input("\ndigite la operacion:").lower()

if operacion == 's':
    suma =  num1 + num2
    print(f"\nEl resultado de la suma es {suma}")
elif operacion == 'r':
    resta = num1 - num2
    print(f"\nEl resultado de la resta es {resta}")
elif operacion == 'm':
    multiplicacion = num1 * num2
    print(f"\nEl resultado de la multiplicacion es {multiplicacion}")
elif operacion == 'd':
    division = num1 / num2
    print(f"\nEl resultado de la division es {division:.2f}")
else:
    print("\nSintax error")
print(f"{sep}Fin de la operacion{sep}")
