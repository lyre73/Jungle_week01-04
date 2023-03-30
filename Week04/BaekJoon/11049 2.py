# # 행렬 곱셈 순서
# #top-down
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N = int(input())
# rc = list(map(int, input().split()))
# for _ in range(N - 1):
#     _, c = input().split()
#     rc.append(int(c))

# dp = [[None] * (N + 1) for _ in range(N + 1)]
# for i in range(N + 1):
#     dp[i][i] = 0

# def mat_slice_mul(left, right):
#     if dp[left][right] != None:
#         return dp[left][right]
#     else:
#         ans = float('inf')
#         for k in range(left, right): # left번 행렬부터 k번 행렬까지 / k+1번 행렬부터 right번 행렬까지
#             tmp = mat_slice_mul(left, k) + mat_slice_mul(k+1, right) + rc[left]*rc[k+1]*rc[right+1]
#             if tmp < ans:
#                 ans = tmp
#         dp[left][right] = ans
#         return ans
# print(mat_slice_mul(0, N-1))


import sys
input = sys.stdin.readline

INF = float('inf')
N = int(input()) # 행렬 1, 1, 2, ... N
rc = list(map(int, input().split()))
for _ in range(N - 1):
    _, c = input().split()
    rc.append(int(c))

dp = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][i] = 0

for L in range(1, N): # right - left (L = 1 ~ N-1):
    # print('L:', L)
    for left in range(1, N - L + 1): # 1 ~ N-L
        right = left + L
        for k in range(left, right):
            # print(f'dp[{left}][{right}] => dp[{left}][{k}] + dp[{k + 1}][{right}] + rc[{left - 1}]*rc[{k}]*rc[{right}])')
            dp[left][right] = min(dp[left][right], dp[left][k] + dp[k + 1][right] + rc[left - 1]*rc[k]*rc[right])
print(dp[1][N])