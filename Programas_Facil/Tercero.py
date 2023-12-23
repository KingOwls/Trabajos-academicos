pesos = []
alturas = []
categorias = {"Bajo peso": 0, "Normal": 0, "Sobrepeso": 0, "Obesidad 1": 0, "Obesidad 2": 0, "Obesidad 3": 0}

for i in range(20):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    edad = int(input(f"Ingrese la edad del estudiante {i+1}: "))
    peso = float(input(f"Ingrese el peso del estudiante {i+1} en kilogramos: "))
    altura = float(input(f"Ingrese la altura del estudiante {i+1} en metros: "))
    imc = peso / altura ** 2
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    elif imc < 35:
        categoria = "Obesidad 1"
    elif imc < 40:
        categoria = "Obesidad 2"
    else:
        categoria = "Obesidad 3"
    categorias[categoria] += 1
    pesos.append(peso)
    alturas.append(altura)

print("Reporte de estado de salud de la comunidad estudiantil:")
print(f"a. {categorias['Normal']} estudiantes se encuentran en el peso ideal.")
print(f"b. {categorias['Obesidad 1']} estudiantes se encuentran en obesidad grado I.")
print(f"c. {categorias['Obesidad 2']} estudiantes se encuentran en obesidad grado II.")
print(f"d. {categorias['Obesidad 3']} estudiantes se encuentran en obesidad grado III.")
print(f"e. {categorias['Sobrepeso']} estudiantes se encuentran en Sobrepeso.")