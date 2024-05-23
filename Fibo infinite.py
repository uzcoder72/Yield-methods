class FibonacciIterator:
    def __init__(self):
        self.prev, self.curr = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.curr
        self.prev, self.curr = self.curr, self.prev + self.curr
        return result
fibonacci_iter = FibonacciIterator()
for i, fib_num in enumerate(fibonacci_iter):
    # if i >= 10:
    #     break
    print(f"Fibonacci {i + 1}: {fib_num}")
