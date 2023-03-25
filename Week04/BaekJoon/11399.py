# ATM
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.sort()
time = 0
ans = 0
for i in range(N):
    time += P[i]
    ans += time
print(ans)