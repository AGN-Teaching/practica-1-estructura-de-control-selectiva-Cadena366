# Pedir al usuario un número
x = input("Introduce un número entre 0 y 36 o 00: ")

# Verificar si el número es 0 o 00
if x == "0":
    print("Paga 0")
elif x == "00":
    print("Paga 00")
else:
    # Convertir el número a entero si no es 0 ni 00
    x = int(x)

    # Mostrar el número único
    print(f"Paga {x}")

    # Verificar si es rojo o negro
    if x in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        print("Paga rojo")
    else:
        print("Paga negro")
    
    # Verificar si es par o impar
    if x % 2 == 0:
        print("Paga par")
    else:
        print("Paga impar")
    
    # Verificar si está en el rango de 1 a 18 o de 19 a 36
    if 1 <= x <= 18:
        print("Paga 1 a 18")
    else:  
        print("Paga 19 a 36")
