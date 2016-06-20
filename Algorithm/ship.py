input()
C = sorted(list(map(int, input().split())))
C_MAX = len(C)
input()
W = sorted(list(map(int, input().split())))
W_MAX = len(W)
is_processed = [False for _ in range(W_MAX)]
W_index, C_index = 0, 0
result = 1

while False in is_processed:
    if W[W_index] > C[-1]:
        result = -1
        break
    elif is_processed[W_index]:
        W_index += 1
        continue
    elif C_index == C_MAX:
        C_index = 0
        result += 1

    if W[W_index] >= C[C_index]:
        for j in range(C_index, C_MAX):
            if W[W_index] <= C[j]:
                C_index = j
                is_processed[W_index] = True
                break
    elif W[W_index] < C[C_index]:
        for j in range(W_MAX - 1, W_index - 1, -1):
            if not is_processed[j] and W[j] <= C[C_index]:
                is_processed[j] = True
                break
    C_index += 1

print(result)
