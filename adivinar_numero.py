import random


# ==============================
# COLORES
# ==============================

RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
CIAN = "\033[96m"
MAGENTA = "\033[95m"


# ==============================
# PRESENTACIÓN
# ==============================

print(f"{AZUL}================================{RESET}")
print(f"""{AZUL}
       ADIVINA EL NÚMERO
       {RESET}""")
print(f"{AZUL}================================{RESET}")


# ==============================
# DATOS DEL JUGADOR
# ==============================

nombre = input("¡Hola! ¿Cómo te llamas?\n")

print(f"Hola {CIAN}{nombre}{RESET} 👋")


# ==============================
# SELECCIÓN DE DIFICULTAD
# ==============================

while True:

    dificultad = input(
        f"{MAGENTA}"
        "ELIGE LA DIFICULTAD:\n"
        "1. FÁCIL\n"
        "2. MEDIO\n"
        "3. DIFÍCIL\n"
        "4. MUY DIFÍCIL\n"
        f"{RESET}"
    )

    # Comprobar que la entrada sea un número
    if not dificultad.isdigit():
        print(f"{ROJO}Debes introducir un número del 1 al 4.{RESET}")
        continue

    dificultad = int(dificultad)

    if dificultad == 1:
        maximo = random.randint(2, 10)
        max_intentos = 5
        break

    elif dificultad == 2:
        maximo = random.randint(10, 100)
        max_intentos = 8
        break

    elif dificultad == 3:
        maximo = random.randint(10, 1000)
        max_intentos = 12
        break

    elif dificultad == 4:
        maximo = random.randint(10, 10000)
        max_intentos = 15
        break

    else:
        print(f"{ROJO}OPCIÓN INCORRECTA. Elige entre 1 y 4.{RESET}")


# ==============================
# GENERAR NÚMERO SECRETO
# ==============================

adivina = random.randint(1, maximo)

print(
    f"\nEstoy pensando en un número entre el 1 y el {maximo}."
    f" Tienes {max_intentos} intentos."
)


# ==============================
# VARIABLES DEL JUEGO
# ==============================

intentos = 0
numeros_descartados = []


# ==============================
# BUCLE PRINCIPAL
# ==============================

while True:

    entrada = input("\n¿Cuál es el número?\n")

    # Comprobar que el jugador introduzca un número
    if not entrada.isdigit():
        print(f"{ROJO}Debes introducir un número.{RESET}")
        continue

    num = int(entrada)


    # ==============================
    # COMPROBAR RANGO
    # ==============================

    if num < 1 or num > maximo:
        print(
            f"{ROJO}"
            f"El número debe estar entre 1 y {maximo}."
            f"{RESET}"
        )
        continue


    # ==============================
    # COMPROBAR NÚMERO REPETIDO
    # ==============================

    if num in numeros_descartados:
        print(f"{ROJO}Ya dijiste este número.{RESET}")
        continue


    # ==============================
    # CONTAR INTENTO
    # ==============================

    intentos += 1
    max_intentos -= 1


    # ==============================
    # COMPROBAR SI GANÓ
    # ==============================

    if num == adivina:

        print(f"{VERDE}¡Correcto!{RESET} 🎉")
        print(f"{VERDE}¡Ganaste!{RESET}")
        print(
            f"{VERDE}"
            f"Lo lograste en {intentos} intentos."
            f"{RESET}"
        )

        break


    # ==============================
    # GUARDAR NÚMERO DESCARTADO
    # ==============================

    numeros_descartados.append(num)
    numeros_descartados.sort()


    # ==============================
    # INDICAR SI ES MAYOR O MENOR
    # ==============================

    if num > adivina:

        print(
            f"{ROJO}"
            f"Incorrecto, el número es menor."
            f" Te quedan {max_intentos} intentos."
            f"{RESET}"
        )

    else:

        print(
            f"{ROJO}"
            f"Incorrecto, el número es mayor."
            f" Te quedan {max_intentos} intentos."
            f"{RESET}"
        )


    # ==============================
    # MOSTRAR NÚMEROS DESCARTADOS
    # ==============================

    nums_string = ", ".join(
        str(numero) for numero in numeros_descartados
    )

    print(
        f"{CIAN}"
        f"Números descartados: {nums_string}"
        f"{RESET}"
    )


    # ==============================
    # COMPROBAR SI SE QUEDÓ SIN INTENTOS
    # ==============================

    if max_intentos == 0:

        print(f"\n{ROJO}¡Perdiste!{RESET}")
        print(
            f"{ROJO}"
            f"Te has quedado sin intentos."
            f" El número era {adivina}."
            f"{RESET}"
        )

        break


    # ==============================
    # GENERAR PISTA CADA 5 INTENTOS
    # ==============================

    if intentos % 5 == 0:

        # Si el número secreto es 1,
        # solo podemos generar una pista de "menor que"
        if adivina == 1:

            pista = random.randint(2, maximo)

            while pista in numeros_descartados:
                pista = random.randint(2, maximo)

            print(
                f"{AMARILLO}"
                f"PISTA: el número es menor que {pista}."
                f"{RESET}"
            )


        # Si el número secreto es igual al máximo,
        # solo podemos generar una pista de "mayor que"
        elif adivina == maximo:

            pista = random.randint(1, maximo - 1)

            while pista in numeros_descartados:
                pista = random.randint(1, maximo - 1)

            print(
                f"{AMARILLO}"
                f"PISTA: el número es mayor que {pista}."
                f"{RESET}"
            )


        # Si está entre los extremos,
        # podemos elegir cualquiera de los dos tipos
        else:

            tipo_pista = random.randint(1, 2)

            if tipo_pista == 1:

                pista = random.randint(1, adivina - 1)

                while pista in numeros_descartados:
                    pista = random.randint(1, adivina - 1)

                print(
                    f"{AMARILLO}"
                    f"PISTA: el número es mayor que {pista}."
                    f"{RESET}"
                )

            else:

                pista = random.randint(adivina + 1, maximo)

                while pista in numeros_descartados:
                    pista = random.randint(adivina + 1, maximo)

                print(
                    f"{AMARILLO}"
                    f"PISTA: el número es menor que {pista}."
                    f"{RESET}"
                )


        # Guardar la pista como número descartado
        numeros_descartados.append(pista)
        numeros_descartados.sort()

        nums_string = ", ".join(
            str(numero) for numero in numeros_descartados
        )

        print(
            f"{CIAN}"
            f"Números descartados: {nums_string}"
            f"{RESET}"
        )