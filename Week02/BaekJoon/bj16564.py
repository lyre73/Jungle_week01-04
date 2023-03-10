# 히오스 프로그래머

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
levels_now = list(map(int, sys.stdin.readlines()))

if N == 1:
    result = N + K
else:
    T_left = min(levels_now)
    T_right = max(levels_now) + K
    while T_left <= T_right:
        T = (T_left + T_right) // 2
        cnt = 0
        for level in levels_now:
            if level < T:
                cnt += T - level
        if cnt <= K: # 올릴 수 있는 레벨보다 필요한 레벨이 작으면
            result = T
            T_left = T + 1
        else:
            T_right = T - 1
print(result)