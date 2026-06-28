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

Consiste en encontrar la menor cantidad de monedas posible para sumar una cantidad determinada de dinero, utilizando un conjunto de valores de monedas disponibles.

Es decir, si tengo 12 centavos, cuál es la cantidad minima de monedas que necesito para completar esos 12 centavos, no importa la denominación (a menos que sea solicitada) sino únicamente la cantidad.

La manera más sencilla y a la vez la menos eficiente que es usando fuerza bruta, es utilizando recursion de manera que, se busque cuál fue la cantidad minima de monedas de los valores anteriores, los valores a comparar son el valor del monto menos los valores de las monedas.

Por ejemplo, si tengo las monedas de valor $1, 2 $ y $5$, si quiero saber cuál es la cantidad minima de monedas de 6 centavos, reviso los valores que cumplan que sea el monto menos cada tipo de moneda:

$6 - 1 = 5$

$6 - 2 = 4$

$6 - 5 = 1$

Una vez identificados los valores previos, reviso cuál de estos me da la minima cantidad de monedas y a esta cantidad le sumo uno (de la moneda a agregar para llegar al monto deseado), esto se hace de manera recursiva hasta tener los valores previos y asi encontrar el minimo.

```
def coin_change(amount, coins):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    minimum = float('inf')
    for coin in coins:
        minimum = min(minimum, coin_change(amount - coin, coins) + 1)

    return minimum
```

Podemos observar que ya cuenta con los casos bases que si hay 0 monedas, pues ahi 0 formas de hacerlo, asi mismo, el caso donde el monto sea negativo donde revuelve con indeterminado, ya que un monto negativo técnicamente es imposible por lo que no se realiza recursion.

Por otro lado, para encontrar el valor se llama nuevamente a la funcion, sin embargo, con el monto modificado como ya se explicó, esta forma es sumamente lenta, ya que realiza calculos repetitivos varias veces como se ve:

![Coin-Minimum.png](Recursos/Moneda/Coin-Minimum.png)

Donde por ejemplo con 6, se realiza 8 veces el cálculo de 1 centavo, lo cual hace que la complejidad se vaya a $O(m^n)$ siendo $m$ la cantidad de posibles llamadas, en este caso que tenemos 3 valores de monedas, $m = 3 $, por lo que la complejidad es $O(3^n)$ siendo sumamente lento, esto se arregla fácilmente usando programacion dinámica.

Caso con memorización:

```
def coin_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    minimum = float('inf')
    for coin in coins:
        minimum = min(minimum, coin_change(amount - coin, coins, memo) + 1)
    memo[amount] = minimum
    return minimum
```

Usando esta técnica podemos ver a simple vista que es muy parecido al anterior o sea el de fuerza bruta; sin embargo, este cuenta con la diferencia de usar un diccionario, el cual va guardando los resultamos de las cantidades mínimas, esto hace que no se tenga que repetir calculos, haciéndolo sumamente menos compleja, siendo de $O(n * m) = O(n)$.

Caso con tabulación:

```
def coin_change(coins, amount):
    if amount < 0:
        return float('inf')
    array = [float('inf')] * (amount + 1)
    array[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                array[i] = min(array[i], array[i - coin] + 1)

    return array[amount]
```

Como tabulación es iterativo, este utiliza dos ciclos `for`, aca creamos una tabla o lista la cual va a ser de tamaño $valor + 1 $, es decir, si el valor es de 6, la lista será de tamaño 7, ya que necesitamos saber los valores de 0 a n. 

Esta lista a diferencia de $fibonacci$ se llena con $inf$ o indeterminado en vez de 0, ya que en caso de hacer una lista de 0 s, esta no servirá, ya que al hacer `min()` siempre será 0.

Por otro lado, los ciclos `for`, uno se encarga de ir recorriendo todos los valoré excepto el 0 el cual ya está agregado desde antes de iterar, hasta el último elemento o sea el valor a encontrar, el otro se encarga de recorrer la lista de monedas dadas para comparar con los valores previos.

Este algoritmo, de igual manera es de complejidad $O(n * m)$, ya que cada ciclo `for` recorre una lista diferente, asi mismo, la lista de monedas que se itera $m$ veces generalemente se da, es decir, el problema nos da de antemano la cantidad de monedas, por lo qeu su complejidad final es de $O(n), $siendo mucho mas eficiente que por fuerza bruta

Tiempo de ejecución con recursividad normal:

![ejecucion-FB.png](Recursos/Moneda/ejecucion-FB.png)

Tiempo de ejecución con Memorización:

![ejecucion-memo.png](Recursos/Moneda/ejecucion-memo.png)

---

### Knapsack (Mochila).
