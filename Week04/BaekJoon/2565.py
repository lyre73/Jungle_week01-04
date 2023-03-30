# # 전깃줄
# import sys
# input = sys.stdin.readline

# N = int(input())
# wires = []
# for _ in range(N):
#     wires.append(tuple(map(int, input().split())))
# wires.sort()

# dp = [1] * N # Ai가 마지막 원소인 LIS 길이

# for i in range(N):
#     x, y = wires[i]
#     for j in range(i):
#         if wires[j][1] < y:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(N - max(dp))



# 전깃줄
import sys, bisect
input = sys.stdin.readline

N = int(input())
wires = []
for _ in range(N):
    wires.append(tuple(map(int, input().split())))
wires.sort()

dp = []

for _, y in wires:
    idx = bisect.bisect_left(dp, y)
    if idx == len(dp):
        dp.append(y)
    else:
        dp[idx] = y
print(N - len(dp))



"""chatGPT code"""
# import sys, bisect
# input = sys.stdin.readline

# # Parse input
# n = int(input())
# wires = [tuple(map(int, input().split())) for _ in range(n)]

# # Sort wires based on the first connection point
# wires.sort(key=lambda x: x[0])

# # Find the longest increasing subsequence of the second connection points
# lis = []
# for _, b in wires:
#     # Use binary search to find the position to insert 'b'
#     idx = bisect.bisect_left(lis, b)
#     if idx == len(lis):
#         lis.append(b)
#     else:
#         lis[idx] = b

# # The answer is the total number of wires minus the length of the LIS
# print(n - len(lis))
