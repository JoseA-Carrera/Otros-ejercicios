'''
*Ejercicio 5
Hacer un programa que pida 3 numeros y determine
cual es el mayor
'''
num1 = float(input("num1 -> "))
num2 = float(input("num2 -> "))
num3 = float(input("num3 -> "))

if num1>=num2 and num1>=num3:
    print(f"{num1:.1f} es el mayor")
elif num2>=num1 and num2>=num3:
    print(f"{num2:.1f} es el mayor")
elif num3>=num1 and num3>=num2:
    print(f"{num3:.1f} es el mayor")
else:
    print("pto el que lea")
