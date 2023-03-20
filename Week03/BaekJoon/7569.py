# 토마토
import sys, collections
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[[None] for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        box[i][j] = list(map(int, input().split()))

# 박스 안에 안 익은 사과가 있는지 판별하는 함수
def no_zero():
        for i in range(H):
            for j in range(N):
                if 0 in box[i][j]:
                    return False
        return True

if no_zero(): # 이미 안 익은 사과가 없으면 계산 없이 바로 0 출력
    print(0)
else:
    # '모든 익은 사과'에서 시작해서 시뮬레이션 돌리기
    def ripe():
        dx = [1, -1, 0, 0, 0, 0]
        dy = [0, 0, 1, -1, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]

        Q = collections.deque()
        for i in range(H):
            for j in range(N):
                for k in range(M):
                    if box[i][j][k] == 1:
                        Q.append((i, j, k))
        while Q:
            u = Q.popleft()
            z, y, x = u
            for dir in range(6):
                vz = z + dz[dir]
                vy = y + dy[dir]
                vx = x + dx[dir]
                if (0 <= vx <= M-1) and (0 <= vy <= N-1) and (0 <= vz <= H-1) and (not box[vz][vy][vx]):
                    Q.append((vz, vy, vx))
                    box[vz][vy][vx] = box[z][y][x] + 1
                    res = box[vz][vy][vx]
        if no_zero():
            return print(res - 1)
        return print(-1)
    ripe()