# # DFS와 BFS
# import sys, collections
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N, M, V = map(int, input().split())
# G = [[] for _ in range(N+1)]

# for line in sys.stdin.readlines():
#     v1, v2 = map(int, line.split())
#     G[v1].append(v2)
#     G[v2].append(v1)

# visit = [True for _ in range(N+1)] # can_visit같은 이름을 쓰고싶다... 하지만 너무 길다...
# def DFS(start):
#     visit[start] = False
#     print(start, end=' ')
#     for i in range(1, N+1):
#         if i in G[start] and visit[i] == True:
#             DFS(i)
# DFS(V)
# print()

# def BFS(start):
#     Q = collections.deque()
#     Q.append(start)
#     visit = [True for _ in range(N+1)]
#     visit[start] = False
#     print(start, end=' ')
#     while Q:
#         for i in range(N+1):
#             if i in G[Q[0]] and visit[i]:
#                 Q.append(i)
#                 visit[i] = False
#                 print(i, end=' ')
#         Q.popleft()
# BFS(V)


# DFS와 BFS
import sys
input = sys.stdin.readline

def DFS(start):
    visited[start] = True
    dfs_ans.append(start)
    for v in sorted(G[start]): # N개 돌리는 것보다 sort-바로 이용이 훠어어어얼씬 빠름
        if not visited[v]:
            DFS(v)

def BFS(start):
    # Q = collections.deque()
    # Q.append(start)
    Q = [start]
    visited[start] = True
    while Q:
        # u = Q.popleft()
        u = Q.pop(0) # ??왜 큐보다 리스트.pop(0)이 더 빠르지??
        bfs_ans.append(u)
        for v in sorted(G[u]): # N개 돌리는 것보다 sort-바로 이용이 훠어어어얼씬 빠름
            if not visited[v]:
                Q.append(v)
                visited[v] = True

N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]

# for line in sys.stdin.readlines():
#     v1, v2 = map(int, line.split())
#     G[v1].append(v2)
#     G[v2].append(v1)

for _ in range(M): # 전부 입력받아서 줄마다 돌리는 것보다 여러번 입력받는 게 야악간 빠를지도
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

# print 반복보다 저장해놓고 나중에 붙여 출력하는 게 빠른듯?
dfs_ans = []
bfs_ans = []

visited = [False] * (N + 1)
DFS(V)
visited = [False] * (N + 1)
BFS(V)

print(*dfs_ans) # unpacking
print(*bfs_ans) # unpacking