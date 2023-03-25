# 가장 긴 증가하는 부분 수열
# bottom-up
import sys
input = sys.stdin.readline

N = int(input())
A = tuple(map(int, input().split()))
DP = [1 for _ in range(N)] # i를 마지막 값으로 가지는 가장 긴 증가하는 부분 수열

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))