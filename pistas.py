import random
import configuracion

def generar_pistas(adivina, maximo, num, numeros_descartados):
    if adivina == 1:
        pista = random.randint(2, maximo)
        while pista in numeros_descartados:
            pista = random.randint(2, maximo)

        print(
            f"{configuracion.AMARILLO}"
            f"PISTA: el número es menor que {pista}."
            f"{configuracion.RESET}"
            )
    elif adivina == maximo:
        pista = random.randint(1, maximo - 1)
        while pista in numeros_descartados:
            pista = random.randint(1, maximo - 1)
        print(
            f"{configuracion.AMARILLO}"
            f"PISTA: el número es mayor que {pista}."
            f"{configuracion.RESET}"
            )
    else:
        tipo_pista = random.randint(1, 8)
        adivina_str = str(adivina)
        pista = None

        if tipo_pista == 1:
            pista = random.randint(1, adivina - 1)
            while pista in numeros_descartados:
                pista = random.randint(1, adivina - 1)
        
            print(
            f"{configuracion.AMARILLO}"
            f"PISTA: el número es mayor que {pista}."
            f"{configuracion.RESET}"
            )
        elif tipo_pista == 2:
            pista = random.randint(adivina + 1, maximo)
            
            while pista in numeros_descartados:
                pista = random.randint(adivina + 1, maximo)
            
            print(
                f"{configuracion.AMARILLO}"
                f"PISTA: el número es menor que {pista}."
                f"{configuracion.RESET}"
                )
        elif tipo_pista == 3:
            if adivina % 2 == 0:
                print(
                    f"{configuracion.AMARILLO}"
                    f"PISTA: el número a adivinar es par"
                    f"{configuracion.RESET}")
            else:
                print(
                    f"{configuracion.AMARILLO}"
                    f"PISTA: el número a adivinar es impar"
                    f"{configuracion.RESET}")
        elif tipo_pista == 4:
            distancia = abs(adivina - num)

            if distancia <= 10:
                print(f"{configuracion.AMARILLO}"
                      f"PISTA: Estás muy cerca"
                      f"{configuracion.RESET}")
            elif (distancia <= 20) and (distancia > 10):
                print(
                    f"{configuracion.AMARILLO}"
                    f"PISTA: Estás cerca"
                    f"{configuracion.RESET}")
            elif (distancia <= 50) and (distancia > 20):
                print(
                    f"{configuracion.AMARILLO}"
                    f"PISTA: Estás un poco lejos"
                    f"{configuracion.RESET}")
            elif (distancia <= 100) and (distancia > 50):
                print(
                    f"{configuracion.AMARILLO}"
                    f"PISTA: Estás lejos"
                    f"{configuracion.RESET}")
            else:
                print(
                    f"{configuracion.AMARILLO}"
                    f"PISTA: Estás muy lejos"
                    f"{configuracion.RESET}")
        elif tipo_pista == 5:
            while True:
                pista_min = random.randint(1, adivina-1)
                pista_max = random.randint(adivina+1, maximo)
        
                if (pista_min not in numeros_descartados) and (pista_max not in numeros_descartados):
                    break
        
        
            print(f"{configuracion.AMARILLO}"
                  f"PISTA: El número está entre {pista_min} y {pista_max}"
                  f"{configuracion.RESET}")
        
            numeros_descartados.append(pista_min)
            numeros_descartados.append(pista_max)
        elif tipo_pista == 6:
            print(f"{configuracion.AMARILLO}"
                  f"PISTA: El número tiene {len(adivina_str)} dígitos"
                  f"{configuracion.RESET}")
        elif tipo_pista == 7:
            posicion = random.randint(0, len(adivina_str)-1)
            digito = adivina_str[posicion]
        
            if posicion == len(adivina_str)-1:
                print(f"{configuracion.AMARILLO}"
                      f"PISTA: El número termina en {digito}"
                      f"{configuracion.RESET}")
            elif posicion == 0:
                print(f"{configuracion.AMARILLO}"
                      f"PISTA: El número empieza en {digito}"
                      f"{configuracion.RESET}")
            else:
                print(f"{configuracion.AMARILLO}"
                      f"PISTA: El número contiene el dígito {digito}"
                      f"{configuracion.RESET}")
        else:
            divisible = random.randint(3, 9)
            if adivina % divisible == 0:
                print(f"{configuracion.AMARILLO}"
                      f"PISTA: El número es divisible por {divisible}"
                      f"{configuracion.RESET}")
            else:
                print(f"{configuracion.AMARILLO}"
                      f"PISTA: El número no es divisible por {divisible}"
                      f"{configuracion.RESET}")

    if pista is not None:
        numeros_descartados.append(pista)

    return numeros_descartados