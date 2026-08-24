# 🎯 Adivina el Número

Un pequeño juego de consola desarrollado en **Python** donde el jugador debe adivinar un número secreto generado aleatoriamente.

El proyecto fue creado como práctica de los fundamentos de Python, incorporando entrada de datos, variables, cadenas de texto, números aleatorios, estructuras de control y debugging.

## 🕹️ ¿Cómo funciona?

Al iniciar el juego:

1. El programa solicita el nombre del jugador.
2. Genera aleatoriamente un límite entre **10 y 100**.
3. Genera un número secreto entre `1` y ese límite.
4. El jugador intenta adivinar el número.
5. El programa indica si el número buscado es mayor o menor.
6. Los números descartados se almacenan y se muestran en pantalla.
7. Después de varios intentos, el programa proporciona una pista.
8. Si el jugador introduce un número que ya fue descartado, se le avisa.
9. Cuando encuentra el número secreto, se muestra el resultado y la cantidad de intentos.

## 🧠 Conceptos de Python utilizados

Este proyecto permite practicar:

* Variables
* `print()`
* `input()`
* Manipulación de cadenas
* f-strings
* Conversión de tipos con `int()`
* Listas
* `append()`
* `sort()`
* Operadores de comparación
* Condicionales `if`, `elif` y `else`
* Bucle `while`
* `break` y `continue`
* Operador `in`
* Módulo `random`
* Debugging y resolución de errores
* Códigos ANSI para colores en consola

## 🎮 Ejemplo

```text
================================

       ADIVINA EL NÚMERO

================================

¡Hola! ¿Cómo te llamas?
Gabriel

Hola Gabriel 👋

Estoy pensando en un número entre el 1 y el 21

¿Cuál es el número?
15

Incorrecto, el número es mayor

Números: 15

¿Cuál es el número?
18

Incorrecto, el número es mayor

Números: 15, 18
```

El objetivo es utilizar la información proporcionada por el programa para ir descartando números hasta encontrar el número secreto.

## 🚀 Posibles mejoras

Algunas ideas para futuras versiones:

* Agregar diferentes niveles de dificultad.
* Limitar la cantidad de intentos.
* Crear un sistema de puntuación.
* Agregar más tipos de pistas.
* Mejorar los colores y la interfaz de la terminal.
* Guardar el mejor resultado.
* Crear un sistema de récords.
* Validar entradas incorrectas para evitar errores cuando el usuario introduce texto.
* Separar el programa en funciones.
* Crear un menú principal.
* Agregar diferentes modos de juego.

## 📚 Objetivo del proyecto

El objetivo principal no es crear un juego complejo, sino utilizarlo como proyecto práctico para aprender y consolidar los fundamentos de programación en Python.

Este proyecto puede evolucionar progresivamente a medida que se incorporen nuevos conceptos al aprendizaje.

## 👨‍💻 Autor

**Gabriel**
