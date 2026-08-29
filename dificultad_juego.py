import random

def establecer_dificultad(dificultad):

    if dificultad == 1:
        maximo = random.randint(2, 10)
        max_intentos = 5

    elif dificultad == 2:
        maximo = random.randint(10, 100)
        max_intentos = 8

    elif dificultad == 3:
        maximo = random.randint(10, 1000)
        max_intentos = 12

    elif dificultad == 4:
        maximo = random.randint(10, 10000)
        max_intentos = 15

    else:
        return None

    return maximo, max_intentos