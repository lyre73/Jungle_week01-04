# 알고리즘 수업 - 피보나치 수 1
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

def fib(n):
    if dp[n] != 0:
        return dp[n]
    if n == 1 or n == 2:
        dp[n] = 1
        return 1
    else:
        dp[n] = fib(n - 1) + fib(n - 2) # ㅇㄴ 얘도 저장해주는걸 까먹었네
        return dp[n]

print(fib(n), n - 2)