# step-tile
#
# 1. List에 순차적으로 입력 받음(size : K)
# 2. 뒤에서 부터 탐색 (오름차순으로 입력되기 때문, K-1 -> K-2 -> … -> 0)
# -> 결과값이 (1 +  ... + 탐색한 값) - (1 + ... + 유효자리 수) 보다 크거나 같을 경우 그냥 break
# 3-1. List[K-1] - List[K-j]를 통해 차이값(d)을 찾음 (j는 2 -> 3 -> ... -> k)
# 3-2. List[K-j-1]부터 K[0]까지 돌면서(x) List[K-1] == x + d일 경우 임시 결과값에 x를 더해주고, 더한 총 횟수도 1 증가시켜주며, d도 d += d.
# 3-3. 임시 결과의 더한 횟수가 3회 이상일 경우 R에 업데이트하고, 아닐 경우 그냥 break.
# 4. '2.'로 돌아감

N = int(input())
L = [int(x) for x in input().split()]
D = {int(x):True for x in L}
R = 0
for i in range(len(L)-1, 1, -1):
    if (L[i] * (L[i] + 1) / 2) - ((L[i] - i - 1) * (L[i] - i) / 2) <= R: break
    for j in range(1, i):
        d = L[i] - L[i-j]
        t = L[i]
        s, c = 0, 0

        while t > 0:
            if t in D:
                s += t
                c += 1
                t -= d
            else:
                break

        if c > 2:
            R = max(R, s)
            if c == i + 1:
                break

print(R)
