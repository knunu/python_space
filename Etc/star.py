i = 0
n = int(input())

while i < n:
    print(' ' * (n-i-1) + '*' * (2*i+1) + ' ' * (n-i-1))
    i += 1