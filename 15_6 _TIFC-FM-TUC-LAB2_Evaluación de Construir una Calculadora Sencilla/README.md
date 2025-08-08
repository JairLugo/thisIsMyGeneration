# Instructions

Write a program that takes two input numbers, then adds them together and prints the result.

**Remember** This project will be automatically graded, and computers are very literal!

## Extra time

If you complete this task then please try adding the following features:

- Take two numbers and subtract the second from the first number.
- Take two numbers and multiply the two.
- Take two numbers and divide the first number by the second number.
- Take two numbers and perform a modulus operation.
- Allow users to choose which operation they want to perform on two numbers.
- Take 3 numbers and add them together.
- Allow users to mix operations with 3 numbers or more
  e.g. 2 + 4 - 3, 4 \*5 + 1 / 3

**Note:** These features must be presented to the user _after_ the initial task, or else the automatic grading will mark this as failed! Scoring for additional features will be done manually.

# Documentación

- En un principio para las tareas 1, 2, 3 y 4 hice las funciones de sumar(), restar(), dividir() y módulo().
- Pero luego pensé con la tarea de módulo sobre el módulo entre cero. No puedes hacer módulo con Cero. Por lo que pregunté a Copilot cómo puedo evitar ese error. Me soltó parte del código que se ve en las líneas 31-33
- Para el menú. Pensé en matar 2 pájaros de 1 tiro, preguntar por la operación y si el usuario quería hacerlo con 2 o 3 variables, después de un rato me di cuenta que estaba haciendo muchas iteraciones if - else Tenía más o menos algo así:

```
if opcion == '1':
    cant = int(input("¿Cuántos valores desea usar? (2 o 3): "))
    if cant == 2:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = sumar(a, b)
    else:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        c = float(input("Ingrese el tercer número: "))
        resultado = sumar(a, b, c)
```

- Por lo que luego le pedí a Copilot que me entregara una manera más limpia de hacer el menú. Me entregó lo que se ve en las líneas 35 a 41. Un ciclo for que itera los inputs que el usuario le entrega al programa y en el menú realiza el cambio más sospechoso.
- Lo que hizo Copilot en las líneas 54 a 73 es que pone las opciones del menú como una lista. Si el usuario pone algo que no debe, el programa te dice que está mal y te saca del programa. Pero si le entrega una de las operaciones correctas, hace la operación
- Cuando Copilot me entrega el código veo algo llamado _continue_ y yo no supe qué era hasta que ví que lo que hace es que sigue con la iteración del ciclo cuando le entregas un valor de la lista.
  [geeksforgeek](https://www.geeksforgeeks.org/python/python-continue-statement/) - link de donde vi la lógica detrás de este statement
  \*Después intenté realizar el punto de realizar la operación con 3 variables. Intenté hacer la lógica con la suma a ver qué tal. Le pregunté a copilot cómo se le hace para aumentarlo. Lo que ves en las lineas 1, 3 y 4 es lo que me modificó copilot. continué esa misma lógica hasta llegar al módulo.
- ¿Cómo le sacas el módulo a un módulo? Un poco irónico la cuestion, ya que el reultado siempre sería 1. Así que, después de 5 minutos intentanto sacar la lógica para rechazar que se hagan módulos entre 3 valores, pregunté con copilot, me entregó las líneas 28 y 29, me estaba acercando.
- Y luego de eso pensé en el menú, por que cuando ejecuté el código pensando sobre cómo pedir los 3 valores. Copilot. Realizo otra pregunta, cuántos números queres usar. Lo que lleva a usar la funcion pedir_numeros(cantidad) y al segundo cambio sospechoso en el menú el (*nums) despues de la funcion.
  [geeksforgeek](https://www.geeksforgeeks.org/python/packing-and-unpacking-arguments-in-python/) - link de donde vi la lógica detrás de los desempaquetados de python.
  *Para la última parte, una amiga me ayudó con la función seguir. Me dijo las lineas 74 a 76 para no slair del programa cuando le pregunté por su visto bueno
