# 피보나치 수 2
import sys
input = sys.stdin.readline

n = int(input())
dp = [None] * (n + 1)
dp[0] = 0
dp[1] = 1

def fibonacci(x):
    if dp[x]:
        return dp[x]

    if x <= 1:
        return dp[x]
    
    dp[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return dp[x]

print(fibonacci(n))