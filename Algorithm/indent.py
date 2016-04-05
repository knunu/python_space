import collections

def find_count(l, p, m):
    if len(Q) == 0: return set_list_count(l, m)
    n = Q.pop()

    if p == 0:
        l.pop(0)
        l.append(n)
        m = abs(n)
        return find_count(l, n, m)
    elif p * n > 0:
        l.append(n)
        m = min(m, abs(n))
        return find_count(l, n, m)
    else:
        Q.append(n)
        return set_list_count(l, m)

def set_list_count(l, m):
    c = 0

    if l[0] > 0:
        for i in range(len(l)): l[i] -= m
    else:
        for i in range(len(l)): l[i] += m
    c += m
    set_stack(l)

    return c

def set_stack(l):
    if len(l) == 0: return

    if l[0] == 0:
        l.pop(0)
        set_stack(l)
    else:
        Q.extend(reversed(l))

N = int(input())
S = list(map(int, input().split()))
D = list(map(int, input().split()))
Q = collections.deque()
v = 0
for i in range(N):Q.append(D[i] - S[i])

while len(Q) != 0:
    p = Q.pop()
    l = [p]
    m = abs(p)
    v += find_count(l, p, m)

print(v)