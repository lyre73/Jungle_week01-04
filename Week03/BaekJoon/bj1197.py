# 최소 스패닝 트리
# 그리디 알고리즘 이용해보기...가 맞나
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
vertice = [True for _ in range(V+1)]
edges = [[] for _ in range(V)]

for _ in range(E):
    v1, v2, w = map(int, input().split())
    edges[v1].append((v2, w))
print(edges)
