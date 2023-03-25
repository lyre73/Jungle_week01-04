# 로프
import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort()

ans = 0
for i in range(1, N + 1): # 쓰는 로프 개수
    ans = max(ans, ropes[-i] * i)
print(ans)