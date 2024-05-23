def fib(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b

generator = fib()
n=int(input("son kiriting: "))
for _ in range(n+1):
    print(next(generator))