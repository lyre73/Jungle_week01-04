# 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for line in sys.stdin.readlines():
    v1, v2 = map(int, line.split())
    G[v1].append(v2)
    G[v2].append(v1)

visit = [True for _ in range(N+1)] # can_visit같은 이름을 쓰고싶다... 하지만 너무 길다...
def DFS(start):
    visit[start] = False
    for i in G[start]: # 이번엔 꼭 번호가 작은 정점부터 가야 하는 건 아니니까
        if visit[i] and not parent[i]:
            parent[i] = start
            DFS(i)
DFS(1)
print("\n".join(map(str, parent[2:])))