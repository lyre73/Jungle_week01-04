# 2xn 타일링
import sys
input = sys.stdin.readline

n = int(input())

DP = [0, 1, 2]
if n <= 2:
    print(DP[n])
else:
    for i in range(3, n + 1):
        DP.append((DP[i - 1] + DP[i - 2]) % 10007)
    print(DP[n])