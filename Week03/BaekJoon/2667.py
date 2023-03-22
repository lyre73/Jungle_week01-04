# 단지번호붙이기
import sys, collections
input = sys.stdin.readline

N = int(input())

G = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def BFS(row, col):
    Q = collections.deque([(row, col)])
    visited[row][col] = True
    home = 1

    while Q:
        ur, uc = Q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = ur + dr, uc + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and G[nr][nc] == 1:
                home += 1
                visited[nr][nc] = True
                Q.append((nr, nc))
    # print(visited)
    return home

cnt = 0
homes = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and G[i][j] == 1:
            # print((i, j))
            homes.append(BFS(i, j))
            cnt += 1
# print(visited)
print(cnt)
print(*sorted(homes), sep='\n')
# print(homes)