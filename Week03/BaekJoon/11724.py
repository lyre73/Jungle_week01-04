# # 연결 요소의 개수(6368ms)
# """BSF 돌리기, 그런데 visit[0]을 제외하고 True가 남아있으면 그걸 다시 시작점으로 해서 BSF 돌리기
# BSF 돌린 횟수를 출력"""

# import sys, collections
# input = sys.stdin.readline

# N, M = map(int, input().split())
# G = [[] for _ in range(N+1)]

# for line in sys.stdin.readlines():
#     v1, v2 = map(int, line.split())
#     G[v1].append(v2)
#     G[v2].append(v1)

# visit = [True for _ in range(N+1)]

# def BFS(start):
#     Q = collections.deque()
#     cnt = 0
#     for j in range(1, N+1):
#         if visit[j]:
#             Q.append(j)
#             visit[j] = False
#             while Q:
#                 for i in range(1, N+1):
#                     if i in G[Q[0]] and visit[i]:
#                         Q.append(i)
#                         visit[i] = False
#                 Q.popleft()
#             cnt += 1
#     return cnt
# if M != 0:
#     print(BFS(1))
# else:
#     print(N)


# # 연결 요소의 개수(700ms)
# """BSF 돌리기, 그런데 visit[0]을 제외하고 True가 남아있으면 그걸 다시 시작점으로 해서 BSF 돌리기
# BSF 돌린 횟수를 출력"""

# import sys, collections
# input = sys.stdin.readline

# def BFS():
#     Q = collections.deque()
#     cnt = 0
#     for i in range(1, N+1):
#         if not visited[i]:
#             Q.append(i)
#             visited[i] = True # 이거랑
#             while Q:
#                 u = Q.popleft()
#                 for v in G[u]:
#                     if not visited[v]:
#                         Q.append(v)
#                         visited[v] = True # 이거를 둘로 나눠서 쓰니까(Q에서 팝할 때 말고 넣을 때 바로 방문 표시) 시간초과 안 남
#             cnt += 1
#     return print(cnt)

# N, M = map(int, input().split())
# G = [[] for _ in range(N+1)]

# for _ in range(M):
#     v1, v2 = map(int, input().split())
#     G[v1].append(v2)
#     G[v2].append(v1)

# visited = [False] * (N + 1)
# visited[0] = True

# BFS()


# # 연결 요소의 개수
# # 다시 풀어보기(669ms)
# """BSF 돌리기, 그런데 visit[0]을 제외하고 True가 남아있으면 그걸 다시 시작점으로 해서 BSF 돌리기
# BSF 돌린 횟수를 출력"""

# import sys, collections
# input = sys.stdin.readline

# def BFS():
#     Q = collections.deque()
#     cnt = 0
#     for i in range(1, N+1):
#         if not visited[i]:
#             Q.append(i)
#             visited[i] = True # 이거랑
#             while Q:
#                 u = Q.popleft()
#                 for v in G[u]: # 이거 개선해서 시간 많이 줄인듯
#                     if not visited[v]:
#                         Q.append(v)
#                         visited[v] = True # 이거를 둘로 나눠서 쓰니까(Q에서 팝할 때 말고 넣을 때 바로 방문 표시) 시간초과 안 남
#             cnt += 1
#     return print(cnt)

# N, M = map(int, input().split())
# G = [[] for _ in range(N+1)]

# for _ in range(M):
#     v1, v2 = map(int, input().split())
#     G[v1].append(v2)
#     G[v2].append(v1)

# visited = [False] * (N + 1)
# visited[0] = True

# BFS()





# 연결 요소의 개수
# 큐 대신 리스트 쓴 풀이(652ms)
"""BSF 돌리기, 그런데 visit[0]을 제외하고 True가 남아있으면 그걸 다시 시작점으로 해서 BSF 돌리기
BSF 돌린 횟수를 출력"""

import sys
input = sys.stdin.readline

def BFS(start):
    # Q = collections.deque()
    # Q.append(start)
    Q = [start]
    visited[start] = True # ! 이거랑
    while Q:
        u = Q.pop(0) # 이건 진짜 왜 더 빠른 거임??? deque.popleft()가 O(1)이고 list.pop(0)가 O(N)인거 아니었어?
        for v in G[u]: # 이거 개선해서 시간 많이 줄인듯
            if not visited[v]:
                Q.append(v)
                visited[v] = True # ! 이거를 둘로 나눠서 쓰니까(Q에서 팝할 때 말고 넣을 때 바로 방문 표시) 시간초과 안 남
            
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

visited = [False] * (N + 1)
visited[0] = True

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        BFS(i)
        cnt += 1
print(cnt)




# # 연결 요소의 개수
# # DSF 쓴 풀이(676ms)
# """DSF 돌리기, 그런데 visit[0]을 제외하고 True가 남아있으면 그걸 다시 시작점으로 해서 DSF 돌리기
# DSF 돌린 횟수를 출력"""

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def DFS(u):
#     visited[u] = True
#     for v in G[u]:
#         if not visited[v]:
#             DFS(v)
            
# N, M = map(int, input().split())
# G = [[] for _ in range(N+1)]

# for _ in range(M):
#     v1, v2 = map(int, input().split())
#     G[v1].append(v2)
#     G[v2].append(v1)

# visited = [False] * (N + 1)

# cnt = 0
# for i in range(1, N+1):
#     if not visited[i]:
#         DFS(i)
#         cnt += 1
# print(cnt)




# # 연결 요소의 개수
# # 서로소 집합 사용(916ms, 메모리 90620KB)
# import sys
# input = sys.stdin.readline

# def find_parent(x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent[x])
#     return parent[x]

# def union_parent(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a
#     return True

# N, M = map(int, input().split())
# G = []
# parent = [i for i in range(N + 1)]

# for _ in range(M):
#     G.append(tuple(map(int, input().split())))

# for edge in G:
#     if find_parent(edge[0]) != find_parent(edge[1]):
#         union_parent(*edge)
# for edge in G:
#     if find_parent(edge[0]) != find_parent(edge[1]):
#         union_parent(*edge)
# print(len(set(parent)) - 1) # 0 제외