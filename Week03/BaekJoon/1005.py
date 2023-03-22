# ACM Craft
import sys, collections
input = sys.stdin.readline

def ACM_Craft():
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
    G = {}
    indegree = [0 for _ in range(N + 1)]
    for i in range(K):
        frm, to = map(int, input().split())
        indegree[to] += 1
        if frm in G.keys():
            G[frm].append(to) # 필요 건물 -> 다음 건물
        else:
            G[frm] = [to]
    target = int(input())

    total_time = [0 for _ in range(N + 1)]
    Q = collections.deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            Q.append(i)
            total_time[i] = build_time[i]
    while Q:
        u = Q.popleft()
        if u == target:
            return print(total_time[u])

        if u in G.keys():
            for v in G[u]:
                indegree[v] -= 1
                total_time[v] = max(total_time[v], total_time[u] + build_time[v]) # oh
                if indegree[v] == 0:
                    Q.append(v)

for _ in range(int(input())):
    ACM_Craft()