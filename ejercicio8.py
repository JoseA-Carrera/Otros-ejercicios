'''
Ejercicio 8 >w<
hacer un programa que simule un cajero automatico con un saldo inicial
de $1000 y tendras el siguiente menu de opciones
1. ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. mostrar dinero disponible
4. salir
'''
saldo = 1000

print(f"\tMENU")
print("1. ingreasar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. mostrar dinero disponible")
print("4. salir")
opcion = int(input("\nDigite una opcion del MENU: "))

if opcion == 1:
    deposito = float(input("Agrege el valor del deposito: "))
    saldo += deposito
    print(f"\nsu saldo actual es de {saldo:.1f}")
elif opcion == 2:
    retiro = float(input("Agrege el valor del retiro: "))
    if retiro>saldo:
        print("No cuentas con esa cantidad de dinero ")
    else:
        saldo -= retiro
        print(f"\nsu saldo actual es de ${saldo:.1f}")
elif opcion == 3:
    print(f"\nsu saldo es de ${saldo:.1f}")
elif opcion == 4:
    print("\nGracias pto")
else:
    print("\nsyntax error xd")
