# 게임을 만든 동준이
import sys
input = sys.stdin.readline

N = int(input())
level = []
for _ in range(N):
    level.append(int(input()))

ans = 0
for i in range(N - 2, -1, -1):
    if level[i] >= level[i + 1]:
        ans += level[i] - level[i + 1] + 1
        level[i] = level[i + 1] - 1
print(ans)