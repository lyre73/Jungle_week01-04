# 동전 2
"""가장 큰 동전의 몫과 나머지를 이용해서 최대한 큰 동전이 많게...?는 아닌것같은데 동전간의 관계도 생각해야함"""
import sys
input = sys.stdin.readline

# 데이터 받기
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# 가격별 필요 동전 개수 초기화
dp = [10001] * (k + 1)
dp[0] = 0

# for i in range(1, k + 1):
#     for coin in coins:
#         dp[i] = min(dp[i], dp[i - coin] + 1)
for coin in coins: # 조심! 위 주석처럼 쓰면 IndexError 발생
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != 10001 else -1)