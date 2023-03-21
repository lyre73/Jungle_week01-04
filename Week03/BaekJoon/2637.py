# 장난감 조립
import sys, collections
input = sys.stdin.readline

N = int(input())
M = int(input())
G = [[] for _ in range(M + 1)]
inorder = [0 for _ in range(M + 1)]
memo = [{} for _ in range(N + 1)]

for _ in range(M):
    X, Y, K = map(int, input().split())
    G[Y].append((X, K)) # Y --K개--> X
    inorder[X] += 1

# 위상 정렬하기
base = []
Q = collections.deque()
for i in range(1, N):
    if inorder[i] == 0:
        Q.append(i)
        base.append(i)
while Q:
    u = Q.popleft()
    if u in base: # 기본 부품이면
        for edge in G[u]:
            v, need = edge
            inorder[v] -= 1
            if inorder[v] == 0:
                Q.append(v)
            memo[v][u] = need
    else: # 중간 부품~완제품이면
        for edge in G[u]:
            v, need = edge
            inorder[v] -= 1
            if inorder[v] == 0:
                Q.append(v)
            for item in memo[u].items():
                if item[0] in memo[v].keys():
                    memo[v][item[0]] += need * item[1]
                else:
                    memo[v][item[0]] = need * item[1]

parts = sorted(memo[-1].items())
for part in parts:
    print(part[0], part[1])