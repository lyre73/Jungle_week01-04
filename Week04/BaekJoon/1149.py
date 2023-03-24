# RGB거리
import sys
input = sys.stdin.readline

INF = float('inf')
N = int(input())
cost = [0] # cost[i][0] = red, [1] = green, [2] = blue
for _ in range(N):
    cost.append(tuple(map(int, input().split())))

DP = [[INF, INF, INF] for _ in range(N + 1)] # DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + cost[i][0]
DP[1] = cost[1]
for i in range(2, N + 1):
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + cost[i][0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + cost[i][1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + cost[i][2]
print(min(DP[N]))