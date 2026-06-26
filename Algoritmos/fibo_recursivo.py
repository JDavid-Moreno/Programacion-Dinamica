def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def main():
    n = 7
    fib = fibo(n)
    print(fib)

main()