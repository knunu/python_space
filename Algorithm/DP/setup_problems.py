""" Runtime Error """
def find_case(n=0, c=0, m=0):
    if n == 0 or c == C-1:
        return n

    if m == 2:
        return n * (find_case(P[c+1], c+1, 0) + find_case(HP[c]-1, c+1, 1) + find_case(HP[c+1], c+1, 2))
    else:
        return n * (find_case(P[c+1], c+1, 0) + find_case(HP[c], c+1, 1) + find_case(HP[c+1], c+1, 2))

C = int(input())
P = [int(x) for x in input().split()]
HP = [int(y) for y in input().split()] + [0]

print(find_case(P[0], 0, 0) % 1000000007)
