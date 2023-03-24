# 1로 만들기 2
import sys
input = sys.stdin.readline

N = int(input())
INF = float('inf')

DP = [0, 0]
to = [None, 0]


for i in range(2, N + 1):
    DP.append(DP[i - 1] + 1)
    to.append(i - 1)
    if not i % 2 and DP[i // 2] + 1 < DP[-1]:
        DP[-1] = DP[i // 2] + 1
        to[-1] = i // 2
    if not i % 3 and DP[i // 3] < DP[-1]:
        DP[-1] = DP[i // 3] + 1
        to[-1] = i // 3

print(DP[N])
idx = N
ans = []
while to[idx] != None:
    ans.append(idx)
    idx = to[idx]
print(*ans, sep=' ')