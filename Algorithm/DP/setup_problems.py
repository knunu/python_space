""" runtime error """
def find_case(n, p_s, s):
    if s:
        if p_s:
            if C_TT[n]: return C_TT[n]
        else:
            if C_FT[n]: return C_FT[n]
        if n == C:
            if p_s == True: return P[n] + AP[n-1]
            else: return P[n] + AP[n-1] - 1
        if P[n] == 0:
            return 0

    else:
        if C_F[n]: return C_F[n]
        if n == C:
            return P[n] + AP[n-1] - 1
        if AP[n] == 0:
            return 0

    if s:
        if p_s:
            C_TT[n] = (P[n] + AP[n-1]) * (find_case(n+1, True, True) + find_case(n+1, True, False)) % 1000000007
            return C_TT[n]
        else:
            C_FT[n] = (P[n] + AP[n-1] - 1) * (find_case(n+1, True, True) + find_case(n+1, True, False)) % 1000000007
            return C_FT[n]
    else:
        C_F[n] = AP[n] * (find_case(n+1, False, True) + find_case(n+1, False, False)) % 1000000007
        return C_F[n]

C = int(input()) - 1
P = [int(x) for x in input().split()]
AP = [int(y) for y in input().split()] + [0]
C_TT = [0] * (C + 1)
C_FT = [0] * (C + 1)
C_F = [0] * (C + 1)

print(P[0] * (find_case(1, True, True) + find_case(1, True, False)) +
      AP[0] * (find_case(1, False, True) + find_case(1, False, False)))
