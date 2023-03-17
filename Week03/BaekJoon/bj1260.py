# DFS와 BFS
import sys, collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]

for line in sys.stdin.readlines():
    v1, v2 = map(int, line.split())
    G[v1].append(v2)
    G[v2].append(v1)

visit = [True for _ in range(N+1)] # can_visit같은 이름을 쓰고싶다... 하지만 너무 길다...
def DFS(start):
    visit[start] = False
    print(start, end=' ')
    for i in range(1, N+1):
        if i in G[start] and visit[i] == True:
            DFS(i)
DFS(V)
print()

def BFS(start):
    Q = collections.deque()
    Q.append(start)
    visit = [True for _ in range(N+1)]
    visit[start] = False
    print(start, end=' ')
    while Q:
        for i in range(N+1):
            if i in G[Q[0]] and visit[i]:
                Q.append(i)
                visit[i] = False
                print(i, end=' ')
        Q.popleft()
BFS(V)