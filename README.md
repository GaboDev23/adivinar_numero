````markdown
# 🎯 Adivina el Número

Un pequeño juego de consola desarrollado en **Python** donde el jugador debe adivinar un número secreto generado aleatoriamente.

El proyecto fue creado como práctica de los fundamentos de Python, incorporando entrada de datos, variables, cadenas de texto, números aleatorios, estructuras de control, listas, debugging, diferentes niveles de dificultad, pistas y colores en la consola.

## 🕹️ ¿Cómo funciona?

Al iniciar el juego:

1. El programa solicita el nombre del jugador.
2. El jugador debe seleccionar un nivel de dificultad.
3. Dependiendo de la dificultad seleccionada, se genera aleatoriamente un límite máximo.
4. Se genera un número secreto entre `1` y el límite máximo.
5. El jugador intenta adivinar el número.
6. El programa indica si el número buscado es mayor o menor que el número introducido.
7. Los números que ya no pueden ser la respuesta se almacenan como números descartados.
8. Los números descartados se ordenan y se muestran en pantalla para ayudar al jugador.
9. Si el jugador introduce un número que ya fue descartado, el programa se lo indica.
10. Cada 5 intentos, el programa proporciona una pista aleatoria.
11. Cuando el jugador encuentra el número secreto, se muestra un mensaje de victoria y la cantidad de intentos realizados.

## 🎚️ Niveles de dificultad

Actualmente el juego cuenta con cuatro niveles de dificultad:

| Dificultad | Rango del límite máximo |
|------------|-------------------------|
| 🟢 Fácil | Entre 2 y 10 |
| 🟡 Medio | Entre 10 y 100 |
| 🟠 Difícil | Entre 10 y 1.000 |
| 🔴 Muy difícil | Entre 10 y 10.000 |

El límite máximo se genera aleatoriamente dentro del rango correspondiente.

Por ejemplo, al seleccionar **Muy difícil**, el programa podría generar:

```text
Estoy pensando en un número entre el 1 y el 8351
````

El número secreto será generado aleatoriamente entre `1` y `8351`.

Si el jugador introduce una opción que no existe, el programa muestra un mensaje de error y vuelve a solicitar la dificultad:

```text
OPCIÓN INCORRECTA
```

## 💡 Sistema de pistas

Después de cada **5 intentos**, el programa genera una pista para ayudar al jugador.

Existen dos tipos de pistas:

```text
PISTA: el número es mayor que 327
```

o:

```text
PISTA: el número es menor que 7642
```

Las pistas se generan aleatoriamente teniendo en cuenta el número secreto.

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
Ya dijiste este número
```

De esta forma se evita repetir números que ya fueron eliminados como posibilidades.

## 🎨 Colores en la consola

El juego utiliza **códigos ANSI** para agregar colores a diferentes elementos de la interfaz de la terminal.

Actualmente se utilizan:

* 🔵 **Azul:** título del juego.
* 🩵 **Cian:** información general y números descartados.
* 🟣 **Magenta:** selección de dificultad.
* 🟡 **Amarillo:** pistas.
* 🔴 **Rojo:** errores y números ya descartados.
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

### Control de flujo

* Condicionales `if`, `elif` y `else`
* Bucles `while`
* `break`
* `continue`

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

El operador módulo se utiliza, entre otras cosas, para determinar cuándo corresponde mostrar una pista:

```python
if intentos != 0 and intentos % 5 == 0:
```

### Otros conceptos

* Debugging y resolución de errores
* Resolución de errores lógicos
* Validación de opciones
* Códigos ANSI para colores en consola
* Construcción de strings a partir de listas
* Uso de `join()` para mostrar los números descartados

## 🎮 Ejemplo

```text
================================

       ADIVINA EL NÚMERO

================================

¡Hola! ¿Cómo te llamas?
Gabriel

Hola Gabriel 👋

ELIGE LA DIFICULTAD:
1. FACIL
2. MEDIO
3. DIFÍCIL
4. MUY DIFÍCIL

4

Estoy pensando en un número entre el 1 y el 8351

¿Cuál es el número?
8000

Incorrecto, el número es menor

Números descartados: 8000

¿Cuál es el número?
6000

Incorrecto, el número es menor

Números descartados: 6000, 8000

¿Cuál es el número?
5000

Incorrecto, el número es menor

Números descartados: 5000, 6000, 8000

...

PISTA: el número es menor que 4500

Números descartados: 1000, 3000, 4500, 5000, 6000, 8000
```

El objetivo es utilizar la información proporcionada por el programa para ir descartando números hasta encontrar el número secreto.

## 📊 Resultado de la partida

Cuando el jugador encuentra el número secreto, el programa muestra un mensaje de victoria junto con la cantidad de intentos realizados:

```text
¡Correcto! 🎉
Ganaste.
Lo lograste en 12 intentos
```

## 🚀 Posibles mejoras

El proyecto puede continuar evolucionando a medida que se incorporen nuevos conceptos de Python.

Algunas ideas para futuras versiones:

* [x] Agregar diferentes niveles de dificultad.
* [ ] Limitar la cantidad de intentos.
* [ ] Crear un sistema de puntuación.
* [ ] Agregar diferentes tipos de pistas.
* [ ] Mejorar los colores y la interfaz de la terminal.
* [ ] Guardar el mejor resultado.
* [ ] Crear un sistema de récords.
* [ ] Validar entradas incorrectas para evitar errores cuando el usuario introduce texto.
* [ ] Evitar errores cuando el usuario introduce números fuera del rango.
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

5. Seguir las instrucciones mostradas en la terminal.

## 👨‍💻 Autor

**Gabriel**

