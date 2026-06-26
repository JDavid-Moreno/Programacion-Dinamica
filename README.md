# Programación Dinámica

---

## Que es?

Es una técnica de diseño de algoritmos que consiste en resolver problemas complejos dividiéndolos en subproblemas más pequeños, la diferencia es que guarda los resultados de esos subproblemas para no necesitar calcularlos nuevamente. 

Su función principal es optimizar, ya que transforma algoritmos que sin programacion dinámica serían muy lenta (crecimiento exponencial) en algoritmos más rápidos (crecimiento lineal o polinómico). Es decir, en lugar de desperdiciar tiempo procesando una y otra vez, la programacion dinámica usa memoria para optimizar y que sea más rapido.

---

## ¿Cuándo se usa?

Para poder aplicar programación dinámica, el problema debe cumplir con dos condiciones:

1. subproblemas superpuestos (Overlapping Subproblems): El problema se puede dividir en subproblemas más pequeños, y esos mismos subproblemas se repiten varias veces durante el cálculo.
2. Substructure óptima (Optimal Substructure): La solución óptima al problema global se puede construir a partir de las soluciones óptimas de sus subproblemas.

---

## Como funciona?

Programación dinámica cuenta con 2 enfoques distintos:

1. Memorización (Top-Down): Este utiliza la estructura recursiva, pero antes de calcular algo, se revisa si ya se guardó en una tabla (que puede ser una lista o un diccionario).
2. Tabulación (Bottom-Up): Este es iterativo, o sea empieza desde los casos más pequeños o los casos base, y se va llenando una tabla hacia arriba hasta llegar al resultado deseado. 

---

## Ejemplos

**NOTA:** Cada ejemplo tendrá su respectiva implementación en python en la carpeta [Algoritmos](https://github.com/JDavid-Moreno/Programacion-Dinamica/tree/main/Algoritmos). 

### Fibonacci 

Este es de los más conocidos, la secuencia de fibonacci consiste en que para encontrar un valor tenemos que sumar los dos elementos anteriores, con base que los primeros dos elementos son 0 y 1, es decir, que fibonacci(0) es 0 y fibonacci(1) es 1, y de ahi se hace la suma.

Por ejemplo, fibonacci(2) es la suma de los anteriores, o sea, fibonacci(1) + fibonacci(0), que es $1 + 0 = 1 $, por lo que, $fibonacci(2) = 1 $.

La manera más sencilla de encontrar cualquier valor de fibonacci es usando recursión, llamando a la misma función pero sumando los valores anteriores.

```
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)
```

De esta manera, a pesar de ser corto, es sumamente deficiente, ya que por ejemplo, si queremos encontrar $fibonacci(5) $, como se puede observar:

![fibonacci.jpeg](Recursos/fibonacci/fibonacci.jpeg)

Cada vez que se llama a la funcion anterior, se repite trabajo, siendo que por ejemplo $fibonacci(1)$ se llama 5 veces, y mientras más grande sea el valor de fibonacci, más trabajo repetitivo se hace, es por eso que la complejidad de este algoritmoe es de $O(2^n)$ siendo muy lento el programa.

Aquí es cuando entra la programacion dinámica, que usando cualquiera de sus 2 metodos mejora grandemente la eficiencia del código.

Usando memorización:

```
def fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

Aquí se usa un diccionario global el cual va guardando los resultados de las iteraciones, esto para que al momento de buscar un valor de fibonacci, si ese valor ya se encuentra en el diccionario, este ya no tenga que calcularlo, sino únicamente tomarlo del diccionario y ya, esto acorta mucho la complejidad del algoritmo a $O(n)$.

Usando Tabulación:

```
def fib(n):
    if n <= 1:
        return n

    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
```

Aquí lo que hacemos es usar una tabla o mejor dicho una lista, esta lista tendrá un tamaño de $n + 1 $ elementos, esto es, ya que evaluaremos desde $0$ a $n$, o sea si $n = 5 $ entonces la lista será: `[0,0,0,0,0,0]`, una vez creada le ingresamos sus valores fijos o base que son el 0 el cual por defecto ya está y el 1 en su respectiva posición.

Una vez con eso podemos realizar una iteración simple usando un ciclo `for` desde el siguiente elemento después del caso base, en este caso 2 hasta el final de la lista, donde para encontrar el elemento siguiente, usamos la suma de fibonacci normal, sumamos los 2 valores anteriores para encontrar el siguiente.

Aquí la diferencia, es que, al hacerlo en una lista con los valores y no de manera recursiva la complejidad baja de igual manera a $O(n)$, siendo mucho más eficiente que por recursividad normal.

Tiempo de ejecución con recursividad normal / Tiempo de ejecución con Tabulación:

![Fibo-recursivo.png](Recursos/fibonacci/Fibo-recursivo.png)
![Fibo-tabulacion.png](Recursos/fibonacci/Fibo-tabulacion.png)

Como se ve, el tiempo de ejecución bajo exageradamente, pasando de más de 10 segundos a menos de 1 milisegundo de ejecución.

---

### Cambio de monedas