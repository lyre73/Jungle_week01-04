# # 트리의 부모 찾기
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N = int(input())
# G = [[] for _ in range(N+1)]
# parent = [0 for _ in range(N+1)]

# for line in sys.stdin.readlines():
#     v1, v2 = map(int, line.split())
#     G[v1].append(v2)
#     G[v2].append(v1)

# visit = [True for _ in range(N+1)] # can_visit같은 이름을 쓰고싶다... 하지만 너무 길다...
# def DFS(start):
#     visit[start] = False # 방문 표시
#     for i in G[start]: # 이번엔 꼭 번호가 작은 정점부터 가야 하는 건 아니니까
#         if visit[i] and not parent[i]:
#             parent[i] = start
#             DFS(i)
# DFS(1)
# print("\n".join(map(str, parent[2:])))
# print(*parent[2:], sep='\n')



# # 트리의 부모 찾기
# # 다시 풀기
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N = int(input())
# G = [[] for _ in range(N+1)]
# parent = [0] * (N + 1)

# for _ in range(N - 1):
#     v1, v2 = map(int, input().split())
#     G[v1].append(v2)
#     G[v2].append(v1)

# visited = [False] * (N + 1)

# def DFS(node):
#     visited[node] = True # 방문 표시
#     for v in G[node]:
#         if not visited[v]:
#             parent[v] = node
#             DFS(v)
# DFS(1)
# print(*parent[2:], sep='\n')


# 트리의 부모 찾기(296ms)
# 다시 풀기, logoo03 참고
import sys, collections
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N+1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

def BFS(node):
    Q = collections.deque([node])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not parent[v]: # if parent[v] == 0 # visited를 parent의 갱신 여부로 파악 가능, visited 리스트 필요없음
                Q.append(v)
                parent[v] = u
BFS(1)
print(*parent[2:], sep='\n') # 간단하게 줄여 출력하기