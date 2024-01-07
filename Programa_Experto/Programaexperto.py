import random

jugadores = {
    "novato": {},
    "intermedio": {},
    "avanzado": {}
}

def registrar_jugador():
    nombre = input("Ingresa el nombre del jugador: ")
    edad = int(input("Ingresa la edad del jugador: "))
    categoria = input("Ingresa la categoría del jugador (novato, intermedio o avanzado): ")
    if categoria not in jugadores:
        print("Categoría inválida.")
        return
    if categoria == "novato" and (edad < 15 or edad > 16):
        print("Edad inválida para la categoría novato.")
        return
    elif categoria == "intermedio" and (edad < 17 or edad > 20):
        print("Edad inválida para la categoría intermedio.")
        return
    elif categoria == "avanzado" and edad <= 20:
        print("Edad inválida para la categoría avanzado.")
        return
    jugadores[categoria][nombre] = {
        "PJ": 0,
        "PG": 0,
        "PP": 0,
        "PA": 0,
        "TP": 0
    }
    print("Jugador registrado con éxito.")

def jugar_partido():
    categoria = input("Ingresa la categoría del partido (novato, intermedio o avanzado): ")
    if categoria not in jugadores:
        print("Categoría inválida.")
        return
    if len(jugadores[categoria]) < 5:
        print("No hay suficientes jugadores inscritos en la categoría.")
        return
    jugador1 = input("Ingresa el nombre del primer jugador: ")
    if jugador1 not in jugadores[categoria]:
        print("Jugador no encontrado.")
        return
    jugador2 = input("Ingresa el nombre del segundo jugador: ")
    if jugador2 not in jugadores[categoria]:
        print("Jugador no encontrado.")
        return
    puntos_j1 = int(input("Ingresa los puntos del primer jugador: "))
    puntos_j2 = int(input("Ingresa los puntos del segundo jugador: "))
    if puntos_j1 == puntos_j2:
        print("Empate.")
        return
    ganador = jugador1 if puntos_j1 > puntos_j2 else jugador2
    perdedor = jugador2 if puntos_j1 > puntos_j2 else jugador1
    jugadores[categoria][ganador]["PJ"] += 1
    jugadores[categoria][ganador]["PG"] += 1
    jugadores[categoria][ganador]["PA"] += puntos_j1 - puntos_j2
    jugadores[categoria][ganador]["TP"] += 2
    jugadores[categoria][perdedor]["PJ"] += 1
    jugadores[categoria][perdedor]["PP"] += 1
    jugadores[categoria][perdedor]["PA"] += puntos_j2 - puntos_j1
    print("Partido registrado con éxito.")

def mostrar_registro():
    print("Registro de jugadores:")
    print("| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format("Categoría", "Jugador", "PJ", "PG", "PP", "PA"))
    for categoria in jugadores:
        for jugador in jugadores[categoria]:
            print("| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format(categoria, jugador, jugadores[categoria][jugador]["PJ"], jugadores[categoria][jugador]["PG"], jugadores[categoria][jugador]["PP"], jugadores[categoria][jugador]["PA"]))

def mostrar_ganador():
    print("Ganadores por categoría:")
    for categoria in jugadores:
        if len(jugadores[categoria]) < 5:
            print("No hay suficientes jugadores inscritos en la categoría {}.".format(categoria))
            continue
        ganador = max