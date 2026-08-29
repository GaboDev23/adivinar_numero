# 🎯 Adivina el Número

Un pequeño juego de consola desarrollado en **Python** donde el jugador debe adivinar un número secreto generado aleatoriamente.

El proyecto fue creado como práctica de los fundamentos de Python, incorporando entrada de datos, variables, cadenas de texto, números aleatorios, estructuras de control, listas, debugging, diferentes niveles de dificultad, sistema de intentos, pistas, validación de entradas, funciones y colores en la consola.

El proyecto comenzó como un juego sencillo y fue evolucionando progresivamente mediante la incorporación y refactorización de diferentes funcionalidades.

## 🕹️ ¿Cómo funciona?

Al iniciar el juego:

1. El programa solicita el nombre del jugador.
2. El jugador debe seleccionar un nivel de dificultad.
3. Dependiendo de la dificultad seleccionada, se genera aleatoriamente un límite máximo.
4. Se genera un número secreto entre `1` y el límite máximo.
5. Dependiendo de la dificultad, se establece una cantidad máxima de intentos.
6. El jugador intenta adivinar el número dentro del límite de intentos disponible.
7. El programa indica si el número buscado es mayor o menor que el número introducido.
8. Los números que ya no pueden ser la respuesta se almacenan como números descartados.
9. Los números descartados se ordenan y se muestran en pantalla para ayudar al jugador.
10. Si el jugador introduce un número que ya fue descartado, el programa se lo indica sin consumir un intento.
11. Si el jugador introduce un valor fuera del rango permitido, se muestra un mensaje de error sin consumir un intento.
12. Si el jugador introduce texto en lugar de un número, se muestra un mensaje de error sin cerrar el programa.
13. Cada 5 intentos, el programa proporciona una pista aleatoria.
14. Las pistas también pueden agregar números a la lista de números descartados.
15. Cuando el jugador encuentra el número secreto, se muestra un mensaje de victoria y la cantidad de intentos realizados.
16. Si el jugador se queda sin intentos, pierde y el programa muestra cuál era el número secreto.

La lógica del juego se encuentra separada en diferentes módulos para facilitar la organización y el mantenimiento del código.

## 📁 Organización del proyecto

El proyecto está dividido en varios archivos Python, cada uno encargado de una parte específica de la aplicación:

```text
AdivinaElNumero/
│
├── main.py
├── juego.py
├── pistas.py
├── dificultad_juego.py
├── configuracion.py
└── README.md
```

### `main.py`

Se encarga de iniciar el programa, mostrar el título, solicitar el nombre del jugador y gestionar la selección de dificultad.

Una vez seleccionada una dificultad válida, obtiene el límite máximo y la cantidad de intentos y comienza la partida mediante:

```python
juego.jugar(maximo, max_intentos)
```

### `dificultad_juego.py`

Contiene la función:

```python
establecer_dificultad()
```

Esta función determina aleatoriamente el límite máximo y establece la cantidad de intentos disponibles según la dificultad seleccionada.

### `juego.py`

Contiene la lógica principal de la partida y varias funciones auxiliares:

```python
mostrar_resultados()
validar_entrada()
mostrar_descartados()
jugar()
```

La función `validar_entrada()` se encarga de comprobar que el valor introducido sea numérico, esté dentro del rango permitido y no haya sido descartado anteriormente.

La función `mostrar_descartados()` se encarga de ordenar y mostrar los números descartados.

La función `mostrar_resultados()` centraliza la impresión de mensajes utilizando los colores definidos en `configuracion.py`.

### `pistas.py`

Contiene la función:

```python
generar_pistas()
```

Esta función genera diferentes tipos de pistas utilizando información del número secreto y devuelve la lista actualizada de números descartados.

De esta manera, el módulo de pistas se encarga exclusivamente de generar la información relacionada con las pistas, mientras que `juego.py` se encarga de gestionar la partida.

### `configuracion.py`

Contiene los códigos ANSI utilizados para los colores de la terminal:

```python
RESET = "\033[0m"

ROJO = "\033[91m"

VERDE = "\033[92m"

AMARILLO = "\033[93m"

AZUL = "\033[94m"

CIAN = "\033[96m"

MAGENTA = "\033[95m"
```

Esto permite reutilizar los mismos colores desde los diferentes módulos.

## 🎚️ Niveles de dificultad

Actualmente el juego cuenta con cuatro niveles de dificultad:

| Dificultad     | Rango del límite máximo | Intentos |
| -------------- | ----------------------- | -------- |
| 🟢 Fácil       | Entre 2 y 10            | 5        |
| 🟡 Medio       | Entre 10 y 100          | 8        |
| 🟠 Difícil     | Entre 10 y 1.000        | 12       |
| 🔴 Muy difícil | Entre 10 y 10.000       | 15       |

Tanto el límite máximo como el número secreto se generan aleatoriamente.

Por ejemplo, al seleccionar **Muy difícil**, el programa podría generar:

```text
Estoy pensando en un número entre el 1 y el 8351. Tienes 15 intentos.
```

El número secreto será generado aleatoriamente entre `1` y `8351`.

Si el jugador introduce una opción que no existe, el programa muestra un mensaje de error y vuelve a solicitar la dificultad:

```text
OPCIÓN INCORRECTA. Elige entre 1 y 4.
```

## 🎯 Sistema de intentos

Cada nivel de dificultad tiene una cantidad determinada de intentos disponibles.

| Dificultad     | Intentos |
| -------------- | -------- |
| 🟢 Fácil       | 5        |
| 🟡 Medio       | 8        |
| 🟠 Difícil     | 12       |
| 🔴 Muy difícil | 15       |

Cada número válido que el jugador introduce y que todavía no había sido descartado consume un intento.

Por ejemplo:

```text
Estoy pensando en un número entre el 1 y el 9. Tienes 5 intentos.

¿Cuál es el número?

3

Incorrecto, el número es mayor.
Te quedan 4 intentos.
```

Los números repetidos no consumen un intento:

```text
¿Cuál es el número?

3

Ya dijiste este número.
```

Tampoco se consume un intento cuando el jugador introduce un valor fuera del rango permitido o una entrada que no sea numérica.

Si el jugador utiliza todos sus intentos sin encontrar el número secreto, la partida termina:

```text
¡Perdiste!

Te has quedado sin intentos.
El número era 742.
```

## 💡 Sistema de pistas

Después de cada **5 intentos**, el programa genera una pista aleatoria.

Actualmente existen **8 tipos diferentes de pistas**.

### 1. Pista de número mayor

Indica que el número secreto es mayor que un número determinado:

```text
PISTA: el número es mayor que 327.
```

### 2. Pista de número menor

Indica que el número secreto es menor que un número determinado:

```text
PISTA: el número es menor que 7642.
```

### 3. Pista de paridad

Indica si el número secreto es par o impar:

```text
PISTA: el número a adivinar es par
```

o:

```text
PISTA: el número a adivinar es impar
```

### 4. Pista de distancia

Compara el número introducido con el número secreto y determina qué tan cerca se encuentra:

```text
PISTA: Estás muy cerca
```

También puede indicar:

```text
PISTA: Estás cerca
```

```text
PISTA: Estás un poco lejos
```

```text
PISTA: Estás lejos
```

```text
PISTA: Estás muy lejos
```

### 5. Pista de rango

Genera dos números, uno menor y otro mayor que el número secreto:

```text
PISTA: El número está entre 327 y 764.
```

Los dos números utilizados para establecer el rango se agregan a los números descartados.

### 6. Pista de cantidad de dígitos

Indica cuántos dígitos tiene el número secreto:

```text
PISTA: El número tiene 4 dígitos
```

### 7. Pista sobre un dígito

Selecciona aleatoriamente una posición del número secreto y muestra información sobre ese dígito.

Puede indicar que:

```text
PISTA: El número empieza en 4
```

```text
PISTA: El número contiene el dígito 7
```

o:

```text
PISTA: El número termina en 2
```

### 8. Pista de divisibilidad

Selecciona aleatoriamente un número entre `3` y `9` y determina si el número secreto es divisible por él:

```text
PISTA: El número es divisible por 5
```

o:

```text
PISTA: El número no es divisible por 5
```

El tipo de pista se selecciona aleatoriamente mediante:

```python
tipo_pista = random.randint(1, 8)
```

El programa también contempla situaciones especiales, como cuando el número secreto es `1` o coincide con el límite máximo, para evitar generar rangos inválidos.

## 🧮 Números descartados

Una de las mecánicas principales del juego es almacenar los números que ya no pueden ser la respuesta.

Por ejemplo:

```text
Números descartados: 15, 30, 48, 70
```

Los números descartados pueden provenir de:

* Números introducidos por el jugador.
* Números utilizados por determinadas pistas.
* Límites proporcionados por algunas pistas de rango.

La función:

```python
mostrar_descartados()
```

se encarga de ordenar y mostrar la lista:

```python
def mostrar_descartados(numeros_descartados):
    numeros_descartados.sort()

    nums_string = ", ".join(
        str(numero) for numero in numeros_descartados
    )

    mostrar_resultados(
        configuracion.CIAN,
        f"Números descartados: {nums_string}"
    )
```

La lista se mantiene ordenada utilizando:

```python
sort()
```

Si el jugador intenta introducir un número que ya fue descartado, el programa muestra:

```text
Ya dijiste este número.
```

De esta forma se evita repetir números que ya fueron eliminados como posibilidades.

## 🛡️ Validación de entradas

La validación de entradas se encuentra separada en la función:

```python
validar_entrada()
```

Esta función recibe los números descartados y el límite máximo permitido y se encarga de validar la entrada antes de devolverla al juego.

### Entrada no numérica

Si el jugador introduce texto:

```text
¿Cuál es el número?

hola
```

El programa muestra:

```text
Debes introducir un número.
```

y vuelve a solicitar una entrada.

### Número fuera del rango

Si el rango permitido es del `1` al `100` y el jugador introduce:

```text
500
```

el programa muestra:

```text
El número debe estar entre 1 y 100.
```

El intento no se consume.

### Número ya descartado

Si el jugador introduce un número que ya se encuentra en la lista:

```text
Ya dijiste este número.
```

El intento tampoco se consume.

Esta separación permite mantener la función `jugar()` más organizada y delegar la responsabilidad de validar entradas a una función específica.

## 🎨 Colores en la consola

El juego utiliza **códigos ANSI** para agregar colores a diferentes elementos de la interfaz de la terminal.

Actualmente se utilizan:

* 🔵 **Azul:** título del juego.
* 🩵 **Cian:** información general y números descartados.
* 🟣 **Magenta:** selección de dificultad.
* 🟡 **Amarillo:** pistas.
* 🔴 **Rojo:** errores y respuestas incorrectas.
* 🟢 **Verde:** victoria y resultado final.

Para evitar repetir constantemente la estructura de impresión de colores, se creó la función:

```python
mostrar_resultados(color, texto)
```

Su funcionamiento es:

```python
def mostrar_resultados(color, texto):
    print(f"{color}{texto}{configuracion.RESET}")
```

Esto permite utilizarla de forma sencilla:

```python
mostrar_resultados(
    configuracion.VERDE,
    "¡Correcto! 🎉"
)
```

## 🧠 Conceptos de Python utilizados

Este proyecto permite practicar diferentes conceptos fundamentales de Python.

### Fundamentos

* Variables.
* `print()`.
* `input()`.
* Manipulación de cadenas.
* f-strings.
* Conversión de tipos con `int()`.
* Validación de entradas.
* Funciones.
* Parámetros.
* Valores de retorno.
* Importación de módulos.

### Control de flujo

* Condicionales `if`, `elif` y `else`.
* Bucles `while`.
* `break`.
* `continue`.
* Operadores lógicos.

### Listas

* Creación y utilización de listas.
* `append()`.
* `sort()`.
* Operador `in`.
* Recorrido de listas.
* Conversión de elementos a texto.

### Números aleatorios

* Importación del módulo `random`.
* `random.randint()`.
* Generación aleatoria del límite máximo.
* Generación aleatoria del número secreto.
* Generación aleatoria de pistas.
* Selección aleatoria del tipo de pista.

### Operadores

* Operadores de comparación.
* Operadores lógicos.
* Operador módulo `%`.
* `abs()` para calcular distancias.

El operador módulo se utiliza para determinar cuándo corresponde mostrar una pista:

```python
if intentos % 5 == 0:
```

### Strings

El método `join()` se utiliza para convertir los números descartados en una cadena:

```python
nums_string = ", ".join(
    str(numero) for numero in numeros_descartados
)
```

Esto permite mostrar la lista de forma más legible en la terminal.

### Modularización

El programa se encuentra dividido en diferentes módulos según la responsabilidad de cada parte:

```text
main.py
    ↓
dificultad_juego.py
    ↓
juego.py
    ↓
pistas.py
```

Esta organización permite evitar concentrar toda la lógica en un único archivo y facilita futuras modificaciones.

## 🔧 Refactorización y mejoras realizadas

Durante el desarrollo se realizaron varias mejoras para organizar el código y reducir la repetición.

### Función `mostrar_resultados()`

Se creó una función para centralizar la impresión de mensajes con colores:

```python
def mostrar_resultados(color, texto):
    print(f"{color}{texto}{configuracion.RESET}")
```

### Función `validar_entrada()`

La validación de los números introducidos por el jugador fue separada de la función principal `jugar()`.

Esto permite que `jugar()` se concentre en la lógica de la partida.

### Función `mostrar_descartados()`

La responsabilidad de ordenar y mostrar los números descartados también fue separada:

```python
mostrar_descartados(numeros_descartados)
```

Esto evita repetir el código encargado de convertir la lista en una cadena y mostrarla.

### Separación del sistema de pistas

El sistema de pistas se mantiene dentro de `pistas.py`.

La función:

```python
generar_pistas()
```

se encarga de generar la pista y devolver la lista actualizada de números descartados.

De esta manera, `juego.py` no necesita conocer los detalles internos de cada tipo de pista.

## 🎮 Ejemplo

```text
================================
       ADIVINA EL NÚMERO
================================

¡Hola! ¿Cómo te llamas?

Gabriel

Hola Gabriel 👋

ELIGE LA DIFICULTAD:

1. FÁCIL
2. MEDIO
3. DIFÍCIL
4. MUY DIFÍCIL

4

Estoy pensando en un número entre el 1 y el 8351.
Tienes 15 intentos.

¿Cuál es el número?

8000

Incorrecto, el número es menor.
Te quedan 14 intentos.

Números descartados: 8000

¿Cuál es el número?

6000

Incorrecto, el número es menor.
Te quedan 13 intentos.

Números descartados: 6000, 8000

¿Cuál es el número?

5000

Incorrecto, el número es menor.
Te quedan 12 intentos.

Números descartados: 5000, 6000, 8000

...

PISTA: el número es menor que 4500.

Números descartados: 4500, 5000, 6000, 8000
```

El objetivo es utilizar la información proporcionada por el programa para ir reduciendo progresivamente las posibilidades hasta encontrar el número secreto.

## 📊 Resultado de la partida

Cuando el jugador encuentra el número secreto, el programa muestra un mensaje de victoria junto con la cantidad de intentos realizados:

```text
¡Correcto! 🎉
¡Ganaste!

Lo lograste en 12 intentos.
```

Si el jugador se queda sin intentos:

```text
¡Perdiste!

Te has quedado sin intentos.
El número era 742.
```

## 🚀 Posibles mejoras

El proyecto puede continuar evolucionando a medida que se incorporen nuevos conceptos de Python.

### Funcionalidades completadas

* [x] Agregar diferentes niveles de dificultad.
* [x] Limitar la cantidad de intentos.
* [x] Agregar diferentes tipos de pistas.
* [x] Mejorar la organización de los colores mediante un módulo de configuración.
* [x] Validar entradas incorrectas.
* [x] Evitar errores cuando se introducen números fuera del rango.
* [x] Separar el programa en funciones.
* [x] Separar la lógica en diferentes módulos.
* [x] Mostrar los números descartados.
* [x] Evitar repetir números descartados.
* [x] Generar pistas automáticamente cada 5 intentos.
* [x] Agregar diferentes categorías de pistas.

### Próximas mejoras

* [ ] Crear un sistema de puntuación.
* [ ] Guardar el mejor resultado.
* [ ] Crear un sistema de récords.
* [ ] Crear un menú principal.
* [ ] Agregar diferentes modos de juego.
* [ ] Permitir jugar nuevamente sin reiniciar el programa.
* [ ] Crear estadísticas de las partidas.
* [ ] Guardar los récords en un archivo.
* [ ] Mejorar la interfaz de la terminal.
* [ ] Agregar una opción para abandonar la partida.
* [ ] Agregar una dificultad personalizada.
* [ ] Mejorar el sistema de generación de pistas.
* [ ] Agregar sonidos o efectos a la interfaz.

## 📚 Objetivo del proyecto

El objetivo principal no es crear un juego complejo, sino utilizarlo como un proyecto práctico para **aprender y consolidar los fundamentos de programación en Python**.

El proyecto comenzó como un juego sencillo de adivinar números y fue evolucionando progresivamente a medida que se incorporaron nuevos conceptos.

Actualmente permite practicar:

* Entrada y salida de datos.
* Variables y tipos de datos.
* Manipulación de cadenas.
* Listas.
* Condicionales.
* Bucles.
* Números aleatorios.
* Operadores.
* Funciones.
* Parámetros y valores de retorno.
* Importación y organización de módulos.
* Debugging.
* Validación de opciones.
* Validación de entradas.
* Validación de rangos.
* Sistema de intentos.
* Sistema de pistas.
* Interfaz de consola.
* Códigos ANSI.
* Organización de la lógica de un programa.
* Modularización y separación de responsabilidades.

La idea es utilizar un proyecto práctico para aplicar los conceptos aprendidos y observar cómo un programa sencillo puede crecer, ser refactorizado y adquirir nuevas funcionalidades con el tiempo.

## 🛠️ Tecnologías utilizadas

* **Python**
* **Visual Studio Code**
* **Git**
* **GitHub**

## 👨‍💻 Autor

**Gabriel**
