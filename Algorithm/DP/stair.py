# def climb(step, mode):
#     if step == 1:
#         return min(climb(step + 1, 1) + S[step], climb(step + 2, 2) + S[step])
#     if mode == 1:
#         return climb(step + 2, 2) + S[step]
#
#     elif mode == 2:
#         if C_2[step] != 0:
#             return C_2[step]
#
#
# S = []
# for _ in range(int(input())):
#     S.append(int(input()))
