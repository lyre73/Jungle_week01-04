# def f(n):
#     temp = []
#     if n <= 0:
#         return [[]]
#     else:
#         for i in range(1, 4):
#             if n - i >= 0:
#                 for item in f(n-i):
#                     temp.append([i] + item)
#         return temp

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     print(len(f(n)))

T = int(input())
P = [0 for _ in range(12)]
P[1] = 1 # 1
P[2] = 2 # 2, 1 1
P[3] = 4 # 3, 2 1, 1 2, 1 1 1
for i in range(4, 12):
    P[i] = P[i-1] + P[i-2] + P[i-3]

for _ in range(T):
    print(P[int(input())])