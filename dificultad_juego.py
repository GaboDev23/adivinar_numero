import random

def establecer_dificultad(dificultad):

    if dificultad == 1:
        maximo = random.randint(2, 10)
        max_intentos = 5
        puntos_base = 500
    elif dificultad == 2:
        maximo = random.randint(10, 100)
        max_intentos = 8
        puntos_base = 1000
    elif dificultad == 3:
        maximo = random.randint(10, 1000)
        max_intentos = 12
        puntos_base = 2000
    elif dificultad == 4:
        maximo = random.randint(10, 10000)
        max_intentos = 15
        puntos_base = 4000
    else:
        return None

    return maximo, max_intentos, puntos_base