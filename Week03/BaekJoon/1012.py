# 유기농 배추
import sys, collections
input = sys.stdin.readline

T = int(input())

def worm(field_col, field_row, num_cabbage):
    field = [[0] * field_col for _ in range(field_row)]
    for _ in range(num_cabbage):
        cab_col, cab_row = map(int, input().split())
        field[cab_row][cab_col] = 1
    
    def BFS(row, col):
        Q = collections.deque([(row, col)])
        field[row][col] = 0

        while Q:
            ur, uc = Q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = ur + dr, uc + dc
                if 0 <= nr < field_row and 0 <= nc < field_col and field[nr][nc] == 1:
                    field[nr][nc] = 0
                    Q.append((nr, nc))
        
    cnt = 0
    for i in range(field_row):
        for j in range(field_col):
            if field[i][j] == 1:
                BFS(i, j)
                cnt += 1
    return cnt

for _ in range(T):
    a, b, c = map(int, input().split())
    print(worm(a, b, c))