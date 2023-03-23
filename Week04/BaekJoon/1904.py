# 01타일
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    if N <= 3:
        return print(N)
    dp = [None] * (N + 1)
    for i in range(1, 4):
        dp[i] = i

    for i in range(4, N + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    return print(dp[N])
sol()

# 1
# 11 00
# 111 001 / 100
# 1111 0011 1001 / 1100 0000
# 11111 00111 10011 11001 00001 / 11100 11011 10000


# 01타일
def sol():
    N = int(input())
    if N <= 3:
        return print(N)
    a, b = 1, 2
    for _ in range(3, N + 1):
        a, b = b, (a + b) % 15746

    return print(b)
sol()