# 연결 요소의 개수
"""BSF 돌리기, 그런데 visit[0]을 제외하고 True가 남아있으면 그걸 다시 시작점으로 해서 BSF 돌리기
BSF 돌린 횟수를 출력"""

import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for line in sys.stdin.readlines():
    v1, v2 = map(int, line.split())
    G[v1].append(v2)
    G[v2].append(v1)

visit = [True for _ in range(N+1)]

def BFS(start):
    Q = collections.deque()
    cnt = 0
    for j in range(1, N+1):
        if visit[j]:
            Q.append(j)
            visit[j] = False
            while Q:
                for i in range(1, N+1):
                    if i in G[Q[0]] and visit[i]:
                        Q.append(i)
                        visit[i] = False
                Q.popleft()
            cnt += 1
    return cnt
if M != 0:
    print(BFS(1))
else:
    print(N)