# 문자열 폭발
import sys
input = sys.stdin.readline

def boom():
    word = input().rstrip()
    bomb = input().rstrip()
    length = len(bomb)
    stack = []

    for char in word:
        stack.append(char)
        if char == bomb[-1]:
            while stack[-length:] == list(bomb):
                for _ in range(length):
                    stack.pop() # 아!!!!!!!!!!!!!!!! stack = stack[:-length]는 오래걸리긴 하겠구나
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')
boom()