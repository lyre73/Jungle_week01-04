# 게임 개발
import sys, collections
input = sys.stdin.readline

N = int(input())
build_time = [0 for _ in range(N + 1)]
G = {}
G_reverse = {}
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
        if i in G_reverse.keys():
            G_reverse[i].append(v) # 다음 건물 -> 필요 건물
        else:
            G_reverse[i] = [v]
# print(indegree)
# print(build_time)

total_time = [0 for _ in range(N + 1)]
Q = collections.deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        Q.append(i)
        total_time[i] = build_time[i]
while Q:
    u = Q.popleft()
    if u in G_reverse.keys():
        temp = 0
        for x in G_reverse[u]:
            temp = max(temp, total_time[x])
        total_time[u] = temp + build_time[u]

    if u in G.keys():
        for v in G[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                Q.append(v)
print(*total_time[1:], sep='\n')