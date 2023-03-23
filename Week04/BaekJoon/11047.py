# 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

ans = 0
for i in range(N - 1, -1, -1):
    K, div = K % coins[i], K // coins[i]
    ans += div
print(ans)