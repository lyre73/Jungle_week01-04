# 점프
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
small = set()
for _ in range(M):
    small.add(int(input()))
dp = {1: {0: 0}}

"""i번 돌에서 출발하는 것부터 전부 계산"""
for now in range(1, N): # 출발 돌 번호: 1~N-1
    if now not in small and now in dp:
        for now_speed in dp[now]:
            for ds in (-1, 0, 1):
                speed = now_speed + ds
                next_stone = now + speed
                if speed >= 1 and next_stone <= N and next_stone not in small:
                    if next_stone in dp: # dp[next_stone] 존재
                        if speed in dp[next_stone]: # dp[next_stone][speed] 존재
                            dp[next_stone][speed] = min(dp[next_stone][speed], dp[now][now_speed] + 1)
                        else: #dp[next_stone]에 아직 speed 없음
                            dp[next_stone][speed] = dp[now][now_speed] + 1
                    else:
                        dp[next_stone] = {speed: dp[now][now_speed] + 1}

print(min(dp[N].values()) if N in dp.keys() else -1)