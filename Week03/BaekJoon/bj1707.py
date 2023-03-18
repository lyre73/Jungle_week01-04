# 이분 그래프
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(node, group):
    visited[node] = group
    for v in G[node]:
        if not visited[v]:
            if group == 1:
                visited[v] = 2
                if DFS(v, 2) == None:
                    return None
            else:
                visited[v] = 1
                if DFS(v, 1) == None:
                    return None
        elif visited[v] == group:
            return None
    return 1

for _ in range(int(input())):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    flag = True
    for i in range(1, V + 1):
        if visited[i] == 0:
            if DFS(i, 1) != 1:
                flag = False
    if flag:
        print("YES")
    else:
        print("NO")