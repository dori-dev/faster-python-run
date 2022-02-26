def fib(n):
    if n < 0:
        return 0
    if n <= 1:
        return n
    first, second = 0, 1
    for _ in range(n):
        first, second = second, first+second
    return first
