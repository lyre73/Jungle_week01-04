# 동전
import sys, collections
input = sys.stdin.readline

def cal(coins, now):
    if now == M:
        return dp[now]
    coins

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1)
    cal(coins, M)