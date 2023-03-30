# 가장 긴 증가하는 부분수열
import sys
input = sys.stdin.readline

N = int(input())
A = tuple(map(int, input().split()))

dp = [1 for _ in range(N)] # i가 마지막인 것 중 가장 긴 증가하는 부분수열의 길이
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
# print(dp)