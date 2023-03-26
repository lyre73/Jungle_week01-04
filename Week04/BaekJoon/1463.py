# 1로 만들기
import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 0]
INF = float('inf')
for i in range(2, N + 1):
    ans1, ans2, ans3 = INF, INF, INF
    if not i % 3:
        ans1 = dp[i // 3] + 1
    if not i % 2:
        ans2 = dp[i // 2] + 1
    ans3 = dp[i - 1] + 1
    dp.append(min(ans1, ans2, ans3))
print(dp[-1])