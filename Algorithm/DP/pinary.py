def fibo(n):
    if n == 1 or n == 2:
        return 1
    if cache[n] != 0:
        return cache[n]
    cache[n] = fibo(n - 2) + fibo(n - 1)
    return cache[n]


N = int(input())
cache = [0 for _ in range(N + 1)]
print(fibo(N))
