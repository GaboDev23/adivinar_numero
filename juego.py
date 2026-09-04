import random
import configuracion
import pistas

def mostrar_resultados(color, texto):
    print(f"{color}{texto}{configuracion.RESET}")

def validar_entrada(numeros_descartados, maximo):
    entrada = 0
    while True:
        entrada = input("\n¿Cuál es el número?\n")
                
        if not entrada.isdigit():
            mostrar_resultados(configuracion.ROJO, "Debes introducir un número.")
            continue

        entrada = int(entrada)

        if entrada < 1 or entrada > maximo:
            mostrar_resultados(configuracion.ROJO, f"El número debe estar entre 1 y {maximo}.")
            continue

        if entrada in numeros_descartados:
            mostrar_resultados(configuracion.ROJO, f"Ya dijiste este número.")
            continue
        break

    return entrada

def mostrar_descartados(numeros_descartados):
    numeros_descartados.sort()

    nums_string = ", ".join(
        str(numero) for numero in numeros_descartados
    )

    mostrar_resultados(
        configuracion.CIAN,
        f"Números descartados: {nums_string}"
    )

def calcular_puntos(puntos_base, intentos_restantes, pistas_usadas):
    return puntos_base + (intentos_restantes * 100) - (pistas_usadas * 50)


def jugar(maximo, max_intentos, puntos_base):
    adivina = random.randint(1, maximo)

    print(
        f"\nEstoy pensando en un número entre el 1 y el {maximo}."
        f" Tienes {max_intentos} intentos."
        )

    intentos = 0
    numeros_descartados = []
    cant_pistas = 0

    while True:
        num = validar_entrada(numeros_descartados, maximo)

        intentos += 1
        max_intentos -= 1

        if num == adivina:
            mostrar_resultados(configuracion.VERDE, "¡Correcto! 🎉\n¡Ganaste!")
            mostrar_resultados(configuracion.VERDE, f"Lo lograste en {intentos} intentos.")
            mostrar_resultados(configuracion.VERDE, f"Puntos: {calcular_puntos(puntos_base, max_intentos, cant_pistas)}")
            break

        numeros_descartados.append(num)

        if num > adivina:
            mostrar_resultados(configuracion.ROJO, f"Incorrecto, el número es menor.\nTe quedan {max_intentos} intentos.")
        else:
            mostrar_resultados(configuracion.ROJO, f"Incorrecto, el número es mayor.\nTe quedan {max_intentos} intentos.")
            
        mostrar_descartados(numeros_descartados)

        if max_intentos == 0:
            mostrar_resultados(configuracion.ROJO, f"¡Perdiste!\nTe has quedado sin intentos.\nEl número era {adivina}")
            mostrar_resultados(configuracion.ROJO, f"Puntos: {calcular_puntos(puntos_base, max_intentos, cant_pistas)}")
            break

        if intentos % 5 == 0:
            numeros_descartados = pistas.generar_pistas(adivina, maximo, num, numeros_descartados)

            cant_pistas += 1

            mostrar_descartados(numeros_descartados)