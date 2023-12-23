total_numeros = 0
total_pares = 0
suma_pares = 0
suma_impares = 0
menores_que_10 = 0
entre_20_y_50 = 0
mayores_que_100 = 0

continuar = True

while continuar:
    numero = int(input("Ingrese un número entero positivo (o un número negativo para salir): "))
    if numero < 0:
        continuar = False
    else:
        total_numeros += 1

        if numero % 2 == 0:
            total_pares += 1
            suma_pares += numero
        else:
            suma_impares += numero

        if numero < 10:
            menores_que_10 += 1
        elif numero >= 20 and numero <= 50:
            entre_20_y_50 += 1
        elif numero > 100:
            mayores_que_100 += 1

if total_numeros == 0:
    print("No se ingresaron números.")
else:
    print(f"Total de números ingresados: {total_numeros}")
    print(f"Total de números pares ingresados: {total_pares}")
    if total_pares == 0:
        print("No se ingresaron números pares.")
    else:
        promedio_pares = suma_pares / total_pares
        print(f"Promedio de los números pares: {promedio_pares}")
    if total_numeros - total_pares == 0:
        print("No se ingresaron números impares.")
    else:
        promedio_impares = suma_impares / (total_numeros - total_pares)
        print(f"Promedio de los números impares: {promedio_impares}")
    print(f"Cantidad de números menores que 10: {menores_que_10}")
    print(f"Cantidad de números entre 20 y 50: {entre_20_y_50}")
    print(f"Cantidad de números mayores que 100: {mayores_que_100}")