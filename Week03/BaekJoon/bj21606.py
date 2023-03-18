# 아침 산책
# 와 방향만 다른 건 어떻게 못 나누나 생각했는데 실외를 한 덩어리로 보는 건 생각 못 함
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def outside(node):
    """서로 연결된 실외를 한 덩어리로 보고, 그 덩어리에 연결된 실내를 반환"""
    inside = set()
    visited.add(node) # 방문 처리
    for v in G[node]:
        if v not in visited:
            visited.add(node)
            if V[v]: # 이 정점이 실내이면
                inside.add(v)
            else: # 이 정점이 실외이면
                inside.update(outside(v))
    return inside

N = int(input()) # 정점의 수
V = [0] + list(map(int, input().rstrip())) # 각 정점이 실내(1)인지, 실외(0)인지
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = set()

way = 0
for i in range(1, N + 1):
    if V[i] == 0 and i not in visited:
        temp = len(outside(i))
        way += temp * (temp - 1)

# 실내-실내 연결도 고려
for i in range(1, N):
    if V[i] == 1:
        for j in G[i]:
            if j > i and V[j] == 1:
                way += 2

print(way)