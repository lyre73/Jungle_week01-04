# 네트워크 연결
import sys
input = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a, b = find_parent(a), find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N = int(input())
M = int(input())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(N + 1)]

cnt = 0
cost = 0
for edge in edges:
    c, a, b = edge
    if find_parent(a) != find_parent(b):
        union(a, b)
        cnt += 1
        cost += c
    if cnt == N - 1:
        break

print(cost)