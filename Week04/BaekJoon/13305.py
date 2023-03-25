# 주유소
import sys
input = sys.stdin.readline

N = int(input())
dist = tuple(map(int, input().split()))
price = tuple(map(int, input().split()))

now = 10 ** 9
ans = 0
for i in range(N - 1):
    now = min(now, price[i])
    ans += now * dist[i]
print(ans)