import random

RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
CIAN = "\033[96m"
MAGENTA = "\033[95m"

print(f"{AZUL}================================{RESET}")
print(F"""{AZUL}
       ADIVINA EL NÚMERO
       {RESET}""")
print(F"{AZUL}================================{RESET}")

nombre = input("¡Hola! ¿Cómo te llamas?\n")

print(f"Hola {CIAN}{nombre}{RESET} 👋")

while True:
    dificultad = int(input(f"{MAGENTA}ELIGE LA DIFICULTAD:\n1. FACIL\n2. MEDIO\n3. DIFÍCIL\n4. MUY DIFÍCIL\n{RESET}"))
    if dificultad == 1:
        max = random.randint(2, 10)
        break
    elif dificultad == 2:
        max = random.randint(10, 100)
        break
    elif dificultad == 3:
        max = random.randint(10, 1000)
        break
    elif dificultad == 4:
        max = random.randint(10, 10000)
        break
    else:
        print(f"{ROJO}OPCIÓN INCORRECTA{RESET}")

print(f"Estoy pensando en un número entre el 1 y el {max}")

adivina = random.randint(1, max)

intentos = 0
nums_string = ""

nums = []

while True:
    num = int(input("¿Cuál es el número?\n"))

    if intentos != 0 and intentos % 5 == 0:
        tipo = random.randint(1, 2)
        pista = -1

        if tipo == 1:
            pista = random.randint(1, adivina-1)
            while pista in nums:
                pista = random.randint(1, adivina-1)
            print(f"{AMARILLO}PISTA: el número es mayor que {pista}{RESET}")
        else:
            pista = random.randint(adivina+1, max)
            while pista in nums:
                pista = random.randint(adivina+1, max)
            print(f"{AMARILLO}PISTA: el número es menor que {pista}{RESET}")
        nums.append(pista)
        nums.sort()
        for i in nums:
            nums_string = ", ".join(str(i) for i in nums)
    
    if num == adivina:
        print(f"{VERDE}¡Correcto! {RESET}🎉")
        print(F"{VERDE}Ganaste.{RESET}")
        print(f"{VERDE}Lo lograste en {intentos} intentos{RESET}")
        break
    elif num in nums:
        print(F"{ROJO}Ya dijiste este número{RESET}")
        continue
    elif num > adivina:
        print(F"{ROJO}Incorrecto, el número es menor{RESET}")
    elif num < adivina:
        print(F"{ROJO}Incorrecto, el número es mayor{RESET}")
    intentos += 1

    nums.append(num)
    nums.sort()
    nums_string = ""
    if len(nums) == 1:
        nums_string = nums[0]
    else:
        for i in nums:
            nums_string = ", ".join(str(i) for i in nums)

    print(f"{CIAN}Números descartados: {nums_string}{RESET}")