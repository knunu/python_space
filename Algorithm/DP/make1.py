def calc(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1

    if n % 3 == 0:
        return calc(n / 3) + 1
    elif n % 2 == 0:
        return min(calc(n / 2) + 1, calc(n - 1) + 1)
    else:
        return calc(n - 1) + 1

print(calc(int(input())))
