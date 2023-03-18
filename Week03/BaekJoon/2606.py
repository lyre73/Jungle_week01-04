# # 바이러스
# import sys, collections
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N = int(input())
# input()
# G = [[] for _ in range(N+1)]

# for line in sys.stdin.readlines():
#     v1, v2 = map(int, line.split())
#     G[v1].append(v2)
#     G[v2].append(v1)

# visit = [True for _ in range(N+1)]

# def BFS(start):
#     Q = collections.deque()
#     Q.append(start)
#     visit[start] = False
#     while Q:
#         for i in range(N+1):
#             if i in G[Q[0]] and visit[i]:
#                 Q.append(i)
#                 visit[i] = False
#         Q.popleft()
# BFS(1)
# print(visit.count(False)-1)


# # 바이러스
# # DFS 사용, 40ms
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N = int(input())
# M = int(input())
# G = [[] for _ in range(N+1)]

# for _ in range(M):
#     v1, v2 = map(int, input().split())
#     G[v1].append(v2)
#     G[v2].append(v1)

# visited = [False] * (N + 1)

# def DFS(node):
#     visited[node] = True
#     for v in G[node]:
#         if not visited[v]:
#             DFS(v)

# DFS(1)

# print(visited.count(True)-1)




# 바이러스
# DFS 사용, rossi22 참고
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

visited = [0] * (N + 1)

def DFS(node):
    visited[node] = 1
    for v in G[node]:
        if not visited[v]:
            DFS(v)

DFS(1)

print(sum(visited)-1)