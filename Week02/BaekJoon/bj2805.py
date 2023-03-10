# 나무 자르기

import sys
input = sys.stdin.readline
    
N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
while True:
    height = (left + right) // 2 # 자르는 높이를 정해 본다
    get = 0 # 얻을 나무의 양 초기화
    for tree in trees: # 이 높이로 잘랐을 때 얻을 나무의 양을 계산한다
        if tree > height:
            get += tree - height
    if get == M: # 목표치만큼 얻으면 자르는 높이를 출력하고 반복을 멈춘다
        print(height)
        break
    elif get < M: # 목표치만큼 못 얻으면 자르는 높이를 낮춘다
        right = height - 1
    else: # 목표치보다 많이 얻으면 자르는 높이를 높인다
        left = height + 1
    
    if left > right: # 딱 목표치만큼 얻을 수는 없으면 
        if get < M:
            print(height-1)
        else:
            print(height)
        break