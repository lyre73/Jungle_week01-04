# 수 찾기

import sys

input = sys.stdin.readline
global A

def find(num):
    """이진 검색"""
    # 왼쪽, 오른쪽 인덱스 초기화
    left = 0
    right = len(A) - 1

    while True: # 값을 찾거나 전부 검색했을때까지 반복
        center = (left + right) // 2 # 중간값 인덱스
        
        if A[center] == num: # 중간값이 목표값이면 있다고 반환, 함수 종료
            return 1
        elif A[center] < num: # 중간값보다 목표값이 크면 왼쪽 인덱스 갱신
            left = center + 1
        else: # 중간값보다 목표값이 작으면 오른쪽 인덱스 갱신
            right = center - 1
        # 왼쪽 인덱스가 오른쪽 인덱스보다 커지면 다 검색한 것, 반복 멈춤
        if right < left:
            break
    # 없다고 반환
    return 0

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
for num in map(int, input().split()):
    print(find(num))