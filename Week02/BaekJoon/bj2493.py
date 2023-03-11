# 탑
"""탑 높이랑 번호를 받아서 튜플로 모아 저장한 다음, 앞에 자기보다 작은 탑 있으면 없애고 없애고... 자기보다 큰 탑 나오면 탑 번호 출력, 자기 푸시"""
import sys
input = sys.stdin.readline

N = int(input())
stack = [] # (탑 높이, 탑 번호) 형태로 저장
i = 0 # 탑 번호를 저장할 변수

for tower in map(int, input().split()):
    i += 1 # 탑 번호 증가
    while stack:
        if stack[-1][0] < tower:
            stack.pop()
        else: # 앞에 자기보다 큰 탑을 발견!
            print(stack[-1][1], end=' ')
            break
    else: # 스택이 비어있으면(앞에 자기보다 큰 탑이 하나도 없음)
        print(0, end=' ')

    stack.append((tower, i))