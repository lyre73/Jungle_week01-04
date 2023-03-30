# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
schedules = []
for _ in range(N):
    start, end = map(int, input().split())
    schedules.append((end, start))
schedules.sort()
ans = 0
last = 0
for end, start in schedules:
    if start >= last:
        ans += 1
        last = end
print(ans)