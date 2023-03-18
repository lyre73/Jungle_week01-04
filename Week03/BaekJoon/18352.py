# 특정 거리의 도시 찾기
import sys, collections
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
G = [[] for _ in range(N+1)]

for line in sys.stdin.readlines():
    v1, v2 = map(int, line.split())
    G[v1].append(v2)

def BFS(start):
    Q = collections.deque()
    visit = [True for _ in range(N+1)]
    dist = [0 for _ in range(N+1)]

    Q.append(start)
    visit[start] = False
    while Q and dist[Q[0]] < K:
        for i in G[Q[0]]:
            if visit[i]:
                Q.append(i)
                visit[i] = False
                if not dist[i]:
                    dist[i] = dist[Q[0]] + 1 
        Q.popleft()
    cnt = dist.count(K)
    # print(dist)
    if cnt:
        for i in range(1, N+1):
            if dist[i] == K:
                print(i)
    else:
        print(-1)
BFS(X)