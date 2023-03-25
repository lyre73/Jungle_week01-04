# 주식
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    stock = [0] + list(map(int, input().split()))
    ans = 0
    max_value = stock[N]
    for i in range(N - 1, 0, -1):
        if stock[i] > max_value:
            max_value = stock[i]
            pass
        elif stock[i] < max_value:
            ans += max_value - stock[i]
    print(ans)