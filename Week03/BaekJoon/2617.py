# 구슬 찾기
# 아이디어 참고
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
ascend = [[] for _ in range(N + 1)] # 가벼운 구슬 -> 무거운 구슬 방향
descend = [[] for _ in range(N + 1)] # 무거운 구슬 -> 가벼운 구슬 방향
ans = 0

for _ in range(M):
    bead1, bead2 = map(int, input().split())
    ascend[bead2].append(bead1)
    descend[bead1].append(bead2)

def DFS_ascend(start):
    """순방향 그래프에서 DFS로 자식 노드 개수 찾기, 돌리기 전에 꼭 visited 갱신해줄 것"""
    cnt = 1
    visited[start] = True
    for v in ascend[start]:
        if not visited[v]:
            cnt += DFS_ascend(v)
    return cnt

def DFS_descend(start):
    """역방향 그래프에서 DFS로 자식 노드 개수 찾기, 돌리기 전에 꼭 visited 갱신해줄 것"""
    cnt = 1
    visited[start] = True
    for v in descend[start]:
        if not visited[v]:
            cnt += DFS_descend(v)
    return cnt

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    a = DFS_ascend(i) - 1 # 함수에서 본인 포함 개수 반환하니까 1 빼주기
    visited = [False] * (N + 1)
    b = DFS_descend(i) - 1
    if a >= (N + 1)//2 or b >= (N + 1)//2:
        ans += 1
print(ans)