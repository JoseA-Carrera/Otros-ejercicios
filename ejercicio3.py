'''
#Ejercicio 3
una tienda ofrece un desucento de 15% sobre el total de la compra
y un cliente desea saber cuanto deberia pagar finalmente por su compra
'''
precio = float(input("Digite el precio: "))

descuento = precio * 0.15
precio_final = precio - descuento

print(f"EL precio final a pagar es de ${precio_final:.2f}")
