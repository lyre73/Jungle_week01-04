# 사냥꾼
"""사대가 아니라 각 동물을 기준으로 잡을 수 있는지(범위 안에 사대가 있는지) 아닌지 확인"""
import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
platform = list(map(int, input().split()))
platform.sort() # ㅇㄴ 이거 까먹었었네 어쩐지 점수가 이상하더라 시간이 부족한 게 아니었구나
animals = [list(map(int, line.split())) for line in sys.stdin.readlines()]
cnt = 0

for animal in animals:
    left_idx = 0
    right_idx = M-1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if platform[mid_idx] < animal[0] + animal[1] - L:
            left_idx = mid_idx + 1
        elif platform[mid_idx] > animal[0] - animal[1] + L:
            right_idx = mid_idx -1
        else:
            cnt += 1
            break
print(cnt)