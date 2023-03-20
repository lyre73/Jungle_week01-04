# 탈출
"""시간에 따른 물의 이동 경로를 전부 구해 둔 다음 고슴도치를 움직이기"""
import sys, collections
input = sys.stdin.readline

R, C = map(int, input().split())
map = [[] for _ in range(R)]

for i in range(R):
    map[i] = list(input().rstrip())

home = None # S가 주어지지 않을 때를 대비
for i in range(R):
    for j in range(C):
        # print(map[i][j])
        if map[i][j] == 'S':
            home = (i, j) # 초기 고슴도치 위치
            map[i][j] = '.'

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 시간에 따른 물의 이동 경로 구하기
def water():
    Q_water = collections.deque()
    for i in range(R):
        for j in range(C):
            if map[i][j] == '*':
                Q_water.append((i, j))
                map[i][j] = 0
    while Q_water:
        r, c = Q_water.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr <= (R - 1)) and (0 <= nc <= (C - 1)) and map[nr][nc] == '.':
                Q_water.append((nr, nc))
                map[nr][nc] = map[r][c] + 1

water()

# 물의 이동 경로를 보고 고슴도치 움직이기
def hedgehog():
    if not home:
        return print('KAKTUS')
    Q_hedgehog = collections.deque()
    Q_hedgehog.append(home)
    map[home[0]][home[1]] = 0
    while Q_hedgehog:
        r, c = Q_hedgehog.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr <= (R - 1)) and (0 <= nc <= (C - 1)):
                if map[nr][nc] == 'D':
                    return print(map[r][c] + 1)
                elif (map[nr][nc] == '.') or ((map[nr][nc] != 'X') and (map[r][c] + 1 < map[nr][nc])):
                    Q_hedgehog.append((nr, nc))
                    map[nr][nc] = map[r][c] + 1
    return print('KAKTUS')

hedgehog()