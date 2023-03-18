# 최소 스패닝 트리
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x] # x~루트까지 전부 루트 노드 번호로 갱신됨

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort(reverse=True)
# edges.sort()
# print(edges)

cost = 0
cnt = 0 # 고른 간선 수
while cnt < V - 1:
    w, u, v = edges.pop()
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        cost += w
        cnt += 1
        # print(f'w:{w}, u:{u}, v:{v}, cost:{cost}, cnt:{cnt}')
        # print(parent)
# for edge in edges:
#     w, u, v = edge
#     if find_parent(parent, u) != find_parent(parent, v):
#         union_parent(parent, u, v)
#         cost += w
#         cnt += 1
#         # print(f'w:{w}, u:{u}, v:{v}, cost:{cost}, cnt:{cnt}')
#         # print(parent)
#     if cnt == V - 1:
#         break
print(cost)