# 피보나치 수 2
# DP, 재귀함수(Top-down)
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




# 피보나치 수 2
# DP, X 재귀(Bottom-up)
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    dp.append(dp[i-1] + dp[i-2])
print(dp[n])




# 피보나치 수 2
import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 1

for i in range(2, n + 1):
    a, b = b, a + b
print(b)