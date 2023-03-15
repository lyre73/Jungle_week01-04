# 스택 수열
import sys
input = sys.stdin.readline

def stacked():
    n = int(input())
    cnt = 1
    stack = [0]
    operator = []

    for _ in range(n):
        digit = int(input())
        if digit == stack[-1]: # 지금 꺼내도 됨
            stack.pop()
            operator.append('-')
        else: # 지금 꺼내면 안 됨
            if digit < cnt: # 근데 이제 집어넣을 수보다도 작음
                return print('NO')
            else:
                while digit != stack[-1]:
                    stack.append(cnt)
                    cnt += 1
                    operator.append('+')
                stack.pop()
                operator.append('-')
    print('\n'.join(operator))
stacked()