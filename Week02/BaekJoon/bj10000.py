# 원 영역
import sys
input = sys.stdin.readline

def circles():
    N = int(input())
    if N == 1:
        return print(2)
    
    data = []

    for _ in range(N):
        x, r = map(int, input().split())
        data.append((x - r, '(')) # x좌표, 열림/닫힘
        data.append((x + r, ')'))
    
    data.sort(key=lambda x: (x[0], -ord(x[1])))
    # print(data)

    stack = []
    area = 0

    for i in range((2 * N) - 1):
        if not stack:
            stack.append([data[i][0], 0])
            # print(stack, i, area)
            continue
        if data[i][1] == '(': # 열린 괄호일 때
            if data[i-1][0] == data[i][0] and stack[-1][1] != -1: # 이전 점과 같은 좌표
                stack[-1][1] = 1
            else: # 이전에 열린 점이 다른 좌표면 무조건 열림 표시(-1)
                stack[-1][1] = -1
            stack.append([data[i][0], 0]) # x좌표, 열려있으면 0, 닫혀있으면 1
            # print(stack, i, area)
        else: # 닫힌 괄호일 때
            if stack[-1][1] == 1: # 닫힌 상태였으면
                area += 2
            else: # 열린 상태였으면
                area += 1
            stack.pop()
            if stack and data[i][0] != data[i+1][0]:
                stack[-1][1] = 0
            # print(stack, i, area)
    if stack[-1][1] == 1:
        area += 2
    else:
        area += 1
    # print(stack, 2*N-1, area)
    
    print(area + 1)

circles()