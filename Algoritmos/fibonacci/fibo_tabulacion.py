def fib(n):
    if n <= 1:
        return n

    array = [0] * (n + 1)
    array[1] = 1
    for i in range(2, n + 1):
        array[i] = array[i - 1] + array[i - 2]
    return array[n]

def main():
    n = 5
    fibo = fib(n)
    print(fibo)

main()