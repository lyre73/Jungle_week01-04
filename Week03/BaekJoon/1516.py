# 게임 개발
import sys, collections
input = sys.stdin.readline

N = int(input())
build_time = [0 for _ in range(N + 1)]
G = {}
# G_reverse = {}
indegree = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    indegree[i] = len(temp[1:-1])
    build_time[i] = temp[0]
    for v in temp[1:-1]:
        if v in G.keys():
            G[v].append(i) # 필요 건물 -> 다음 건물
        else:
            G[v] = [i]

total_time = [0 for _ in range(N + 1)]
Q = collections.deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        Q.append(i)
        total_time[i] = build_time[i]
while Q:
    u = Q.popleft()

    if u in G.keys():
        for v in G[u]:
            indegree[v] -= 1
            total_time[v] = max(total_time[v], total_time[u] + build_time[v]) # oh
            if indegree[v] == 0:
                Q.append(v)
print(*total_time[1:], sep='\n')