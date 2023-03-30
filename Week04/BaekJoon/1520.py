# 내리막 길
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
geo = []
for _ in range(M):
    geo.append(list(map(int, input().split())))

dp = [[-1] * N for _ in range(M)] # dp[i][j] = i, j에서 오른쪽 아래 끝까지 가는 경로 개수

def DFS(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    
    if r == M-1 and c == N-1: # 도착
        dp[r][c] = 1
        return 1 # dp[r][c]
    else:
        dp[r][c] = 0
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N and geo[nr][nc] < geo[r][c]:
                dp[r][c] += DFS(nr, nc)

        if dp[r][c] == -1:
            return 0
        else:
            return dp[r][c]
print(DFS(0, 0))