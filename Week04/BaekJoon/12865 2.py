# 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
articles = []
for _ in range(N):
    articles.append(tuple(map(int, input().split())))

dp = [0] * (K + 1)

for article in articles:
    weight, val = article
    for i in range(K, weight-1, -1):
        dp[i] = max(dp[i], dp[i - weight] + val)
print(dp[K])