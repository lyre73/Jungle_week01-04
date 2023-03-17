# 바이러스
import sys, collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
input()
G = [[] for _ in range(N+1)]

for line in sys.stdin.readlines():
    v1, v2 = map(int, line.split())
    G[v1].append(v2)
    G[v2].append(v1)

visit = [True for _ in range(N+1)]

def BFS(start):
    Q = collections.deque()
    Q.append(start)
    visit[start] = False
    while Q:
        for i in range(N+1):
            if i in G[Q[0]] and visit[i]:
                Q.append(i)
                visit[i] = False
        Q.popleft()
BFS(1)
print(visit.count(False)-1)