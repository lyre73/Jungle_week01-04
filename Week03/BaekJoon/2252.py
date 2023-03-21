# 줄 세우기
import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
inorder = [0 for _ in range(N + 1)] # 진입 차수 저장
line = [] # 세운 줄 저장

# 간선 및 진입 차수 저장
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    inorder[b] += 1

# 위상 정렬
def topological_sort():
    Q = collections.deque() # 진입 차수가 0이 된 노드들을 차례로 넣기
    for i in range(1, N + 1): # 초기 진입 차수 0인 노드들 넣기
        if inorder[i] == 0:
            Q.append(i)
    
    while Q:
        u = Q.popleft()
        line.append(u)
        for v in G[u]:
            if inorder[v] > 1:
                inorder[v] -= 1
            elif inorder[v] == 1: # 새로 진입 차수가 0이 된 노드를 Q에 넣기
                inorder[v] -= 1
                Q.append(v)

topological_sort()
print(*line, sep=' ')