# 미로만들기
"""데이크스트라/다익스트라로 각 정점마다 뚫고 온 벽의 개수를 갱신, 뚫은 벽의 개수를 기준으로 한 최소 우선순위 큐 이용"""
import sys, heapq
input = sys.stdin.readline

n = int(input())
G = []
for _ in range(n):
    G.append(list(map(int,input().rstrip())))

# print(*G, sep='\n')
broke = [[float("inf") for _ in range(n)] for _ in range(n)]
broke[0][0] = 0
start = (0, 0)
end = (n - 1, n - 1)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

Q = [(0, (0, 0))]

while Q:
    _, room = heapq.heappop(Q)
    for i in range(4):
        v = (room[0] + dy[i], room[1] + dx[i])
        if (0 <= v[0] <= n - 1) and (0 <= v[1] <= n - 1):
            if G[v[0]][v[1]] == 0:
                temp = broke[room[0]][room[1]] + 1
            else:
                temp = broke[room[0]][room[1]]
            if temp < broke[v[0]][v[1]]:
                heapq.heappush(Q, (temp, (v[0], v[1])))
                broke[v[0]][v[1]] = temp
print(broke[n-1][n-1])