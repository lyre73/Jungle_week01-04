# 미로 탐색
import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(N):
    G[i] = list(map(int, input().rstrip()))

dr = [1, 0, -1, 0] # delta row
dc = [0, 1, 0, -1] # delta column

def BFS(row, col):
    Q = collections.deque([(row, col)]) # 시작 지점으로 큐 초기화
    while Q:
        ur, uc = Q.popleft() # u row, column
        for i in range(4):
            vr = ur + dr[i] # v row
            vc = uc + dc[i] # v column
            if (-1 < vr < N) and (-1 < vc < M) and G[vr][vc] == 1: # 방문 여부는 숫자가 1인지 아닌지로 판단(처음 한 칸은 다시 탐색하지만 결과에 영향 없음)
                if vr == N - 1 and vc == M - 1: # 목적지 도착
                    return print(G[ur][uc] + 1) # 출력하고 함수 종료(반드시 도착하는 입력값만 주어지기 때문에 무한루프 돌 일 없음)
                G[vr][vc] = G[ur][uc] + 1 # 이 노드의 값(지난 칸 수) 갱신
                Q.append((vr, vc))
    
BFS(0, 0)