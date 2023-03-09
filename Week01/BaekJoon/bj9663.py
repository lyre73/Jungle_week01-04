# # # N-Queen
# N = int(input())

# global cnt, pos
# pos = [None] * N
# cnt = 0

# def n_queen(i, pos):
#     global cnt
#     if can_set(i, pos):
#         if i == len(pos) - 1:
#             cnt += 1
#             # print(pos)
#         else:
#             for j in range(len(pos)): # 0, 1, 2, ... , N-1
#                 pos[i+1] = j
#                 n_queen(i+1, pos)
#     else:
#         return

# def can_set(i, pos): # 계산량? 메모리?를 줄인 flag
#     # if i == 0:
#     #     return True
#     k = 0
#     flag = True
#     while k < i and flag: # k = 1, 2, ... , i-1
#         if pos[k] == pos[i] or abs(pos[k] - pos[i]) == i - k:
#             flag = False
#         k += 1
#     return flag

# n_queen(-1, pos)
# print(cnt)



N = int(input())

