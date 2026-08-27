# 🎯 Adivina el Número

Un pequeño juego de consola desarrollado en **Python** donde el jugador debe adivinar un número secreto generado aleatoriamente.

El proyecto fue creado como práctica de los fundamentos de Python, incorporando entrada de datos, variables, cadenas de texto, números aleatorios, estructuras de control, listas, debugging, diferentes niveles de dificultad, sistema de intentos, pistas y colores en la consola.

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
14. Cuando el jugador encuentra el número secreto, se muestra un mensaje de victoria y la cantidad de intentos realizados.
15. Si el jugador se queda sin intentos, pierde y el programa muestra cuál era el número secreto.

## 🎚️ Niveles de dificultad

Actualmente el juego cuenta con cuatro niveles de dificultad:

| Dificultad | Rango del límite máximo | Intentos |
|------------|-------------------------|----------|
| 🟢 Fácil | Entre 2 y 10 | 5 |
| 🟡 Medio | Entre 10 y 100 | 8 |
| 🟠 Difícil | Entre 10 y 1.000 | 12 |
| 🔴 Muy difícil | Entre 10 y 10.000 | 15 |

Tanto el límite máximo como el número secreto se generan aleatoriamente.

Por ejemplo, al seleccionar **Muy difícil**, el programa podría generar:

```text
Estoy pensando en un número entre el 1 y el 8351. Tienes 15 intentos.
````

El número secreto será generado aleatoriamente entre `1` y `8351`.

Si el jugador introduce una opción que no existe, el programa muestra un mensaje de error y vuelve a solicitar la dificultad:

```text
OPCIÓN INCORRECTA
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

Incorrecto, el número es mayor. Te quedan 4 intentos.
```

Los números repetidos no consumen un intento:

```text
¿Cuál es el número?
3

Ya dijiste este número.
```

De esta forma, el jugador no es penalizado por introducir accidentalmente un número que ya había descartado.

Tampoco se consume un intento cuando el jugador introduce un valor fuera del rango permitido o una entrada que no sea numérica.

Si el jugador utiliza todos sus intentos sin encontrar el número secreto, la partida termina:

```text
¡Perdiste!

Te has quedado sin intentos. El número era 742.
```

## 💡 Sistema de pistas

Después de cada **5 intentos**, el programa genera una pista para ayudar al jugador.

Existen dos tipos de pistas:

```text
PISTA: el número es mayor que 327.
```

o:

```text
PISTA: el número es menor que 7642.
```

Las pistas se generan aleatoriamente teniendo en cuenta el número secreto.

El programa también contempla situaciones especiales, como cuando el número secreto es `1` o coincide con el límite máximo, para evitar generar rangos inválidos.

Por ejemplo, si el número secreto es `500`:

```text
PISTA: el número es mayor que 327.
```

Esto permite descartar todos los números menores o iguales a `327`.

Los números utilizados como pistas también se agregan a la lista de números descartados, ya que el número indicado en la pista no puede ser el número secreto.

## 🧮 Números descartados

Una de las mecánicas principales del juego es almacenar los números que ya no pueden ser la respuesta.

Por ejemplo:

```text
Números descartados: 15, 30, 48, 70
```

Esto permite que el jugador utilice la información proporcionada por el programa para reducir progresivamente las posibilidades.

Los números descartados pueden provenir tanto de los números introducidos por el jugador como de las pistas proporcionadas por el programa.

Los números se mantienen ordenados utilizando `sort()`.

Si el jugador intenta introducir un número que ya fue descartado, el programa muestra:

```text
Ya dijiste este número.
```

De esta forma se evita repetir números que ya fueron eliminados como posibilidades.

## 🎨 Colores en la consola

El juego utiliza **códigos ANSI** para agregar colores a diferentes elementos de la interfaz de la terminal.

Actualmente se utilizan:

* 🔵 **Azul:** título del juego.
* 🩵 **Cian:** información general y números descartados.
* 🟣 **Magenta:** selección de dificultad.
* 🟡 **Amarillo:** pistas.
* 🔴 **Rojo:** errores, respuestas incorrectas y números ya descartados.
* 🟢 **Verde:** victoria y resultado final.

Los colores se implementan mediante variables:

```python
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
CIAN = "\033[96m"
MAGENTA = "\033[95m"
```

## 🧠 Conceptos de Python utilizados

Este proyecto permite practicar:

### Fundamentos

* Variables
* `print()`
* `input()`
* Manipulación de cadenas
* f-strings
* Conversión de tipos con `int()`
* Validación de entradas

### Control de flujo

* Condicionales `if`, `elif` y `else`
* Bucles `while`
* `break`
* `continue`
* Operadores lógicos

### Listas

* Creación y utilización de listas
* `append()`
* `sort()`
* Operador `in`

### Números aleatorios

* Importación de módulos
* Módulo `random`
* `random.randint()`
* Generación aleatoria del límite máximo
* Generación aleatoria del número secreto
* Generación aleatoria de pistas
* Selección aleatoria del tipo de pista

### Operadores

* Operadores de comparación
* Operadores lógicos
* Operador módulo `%`

El operador módulo se utiliza para determinar cuándo corresponde mostrar una pista:

```python
if intentos % 5 == 0:
```

### Otros conceptos

* Debugging y resolución de errores
* Resolución de errores lógicos
* Validación de opciones
* Validación de entradas
* Validación de rangos
* Códigos ANSI para colores en consola
* Construcción de strings a partir de listas
* Uso de `join()` para mostrar los números descartados

## 🛡️ Validación de entradas

El programa incluye diferentes validaciones para evitar que errores de entrada interrumpan la partida.

### Entrada no numérica

Si el jugador introduce texto:

```text
¿Cuál es el número?
hola
```

El programa muestra un mensaje de error y vuelve a solicitar el número.

### Número fuera del rango

Si el rango permitido es del `1` al `100` y el jugador introduce:

```text
¿Cuál es el número?
500
```

El programa muestra:

```text
El número debe estar entre 1 y 100.
```

El intento no se consume.

### Opción de dificultad inválida

Si el jugador introduce una dificultad que no existe:

```text
ELIGE LA DIFICULTAD:
1. FÁCIL
2. MEDIO
3. DIFÍCIL
4. MUY DIFÍCIL

5

OPCIÓN INCORRECTA.
```

El programa vuelve a solicitar una dificultad válida.

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

Estoy pensando en un número entre el 1 y el 8351. Tienes 15 intentos.

¿Cuál es el número?
8000

Incorrecto, el número es menor. Te quedan 14 intentos.

Números descartados: 8000

¿Cuál es el número?
6000

Incorrecto, el número es menor. Te quedan 13 intentos.

Números descartados: 6000, 8000

¿Cuál es el número?
5000

Incorrecto, el número es menor. Te quedan 12 intentos.

Números descartados: 5000, 6000, 8000

...

PISTA: el número es menor que 4500.

Números descartados: 1000, 3000, 4500, 5000, 6000, 8000
```

El objetivo es utilizar la información proporcionada por el programa para ir descartando números hasta encontrar el número secreto.

## 📊 Resultado de la partida

Cuando el jugador encuentra el número secreto, el programa muestra un mensaje de victoria junto con la cantidad de intentos realizados:

```text
¡Correcto! 🎉
Ganaste.
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

Algunas ideas para futuras versiones:

* [x] Agregar diferentes niveles de dificultad.
* [x] Limitar la cantidad de intentos.
* [ ] Agregar diferentes tipos de pistas.
* [ ] Mejorar los colores y la interfaz de la terminal.
* [ ] Validar entradas incorrectas para evitar errores cuando el usuario introduce texto.
* [ ] Evitar errores cuando el usuario introduce números fuera del rango.
* [ ] Crear un sistema de puntuación.
* [ ] Guardar el mejor resultado.
* [ ] Crear un sistema de récords.
* [ ] Separar el programa en funciones.
* [ ] Crear un menú principal.
* [ ] Agregar diferentes modos de juego.
* [ ] Permitir jugar nuevamente sin reiniciar el programa.
* [ ] Crear estadísticas de las partidas.
* [ ] Guardar los récords en un archivo.

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
* Debugging.
* Validación de opciones.
* Validación de entradas.
* Validación de rangos.
* Sistema de intentos.
* Sistema de pistas.
* Interfaz de consola.
* Códigos ANSI.
* Organización de la lógica de un programa.

Este proyecto puede seguir evolucionando progresivamente a medida que se incorporen nuevos conceptos al aprendizaje.

La idea es utilizar un proyecto práctico para aplicar los conceptos aprendidos y observar cómo un programa sencillo puede crecer y adquirir nuevas funcionalidades con el tiempo.

## 🛠️ Tecnologías utilizadas

* **Python**
* **Visual Studio Code**
* **Git**
* **GitHub**

## 👨‍💻 Autor

**Gabriel**
