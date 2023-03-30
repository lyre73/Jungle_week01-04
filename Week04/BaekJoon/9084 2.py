# 동전
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    coins = tuple(map(int, input().split()))
    money = int(input())
    dp = [0] * (money + 1) # idx 0 ~ money
    dp[0] = 1
    for coin in coins:
        for i in range(coin, money + 1):
            dp[i] += dp[i - coin]
    print(dp[-1])