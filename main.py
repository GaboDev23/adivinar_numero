import configuracion
import dificultad_juego
import juego

print(f"{configuracion.AZUL}================================{configuracion.RESET}")
print(f"""{configuracion.AZUL}
       ADIVINA EL NÚMERO
       {configuracion.RESET}""")
print(f"{configuracion.AZUL}================================{configuracion.RESET}")

nombre = input("¡Hola! ¿Cómo te llamas?\n")

print(f"Hola {configuracion.CIAN}{nombre}{configuracion.RESET} 👋")

while True:
    dificultad = input(
        f"{configuracion.MAGENTA}"
        "ELIGE LA DIFICULTAD:\n"
        "1. FÁCIL\n"
        "2. MEDIO\n"
        "3. DIFÍCIL\n"
        "4. MUY DIFÍCIL\n"
        f"{configuracion.RESET}"
    )

    if not dificultad.isdigit():
        print(f"{configuracion.ROJO}Debes introducir un número del 1 al 4.{configuracion.RESET}")
        continue

    dificultad = int(dificultad)

    resultado = dificultad_juego.establecer_dificultad(dificultad)

    if resultado is None:
        print(
            f"{configuracion.ROJO}"
            "OPCIÓN INCORRECTA. Elige entre 1 y 4."
            f"{configuracion.RESET}"
            )
        continue

    maximo, max_intentos = resultado
    break

juego.jugar(maximo, max_intentos)