# 연산자 끼워넣기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_ans = float("-inf")
min_ans = float("inf")

def operate(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a - b
    elif operator == 2:
        return a * b
    else:
        if a < 0 and b > 0:
            return -((-a) // b)
        else:
            return a // b

def DFS(prev_res, idx): # idx: 1 ~ N-1
    if idx == N-1:
        global max_ans, min_ans
        # print(operators)
        for i in range(4):
            # print(i)
            if operators[i]:
                ans = operate(prev_res, A[idx], i)
                # print(ans)
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        # print(max_ans, min_ans)
        return
    
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            DFS(operate(prev_res, A[idx], i), idx + 1)
            operators[i] += 1

DFS(A[0], 1)

print(max_ans, min_ans, sep="\n")