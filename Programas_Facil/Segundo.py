nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
peso = float(input("Ingrese el peso del estudiante en kilogramos: "))
altura = float(input("Ingrese la altura del estudiante en metros: "))

imc = peso / altura**2

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

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"IMC: {imc:.2f}")
print(f"Categoría: {categoria}")