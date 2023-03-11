# 괄호의 값
import sys

brackets = sys.stdin.readline().strip()
stk = []
ans = 0
temp = 1

for idx in range(len(brackets)):
    if brackets[idx] == '(':
        stk.append(brackets[idx])
        temp *= 2
    elif brackets[idx] == '[':
        stk.append(brackets[idx])
        temp *= 3
    elif brackets[idx] == ')':
        if not stk or stk[-1] != '(':
            ans = 0
            break
        elif brackets[idx-1] == '(':
            ans += temp
        stk.pop()
        temp //= 2
    else:
        if not stk or stk[-1] != '[':
            ans = 0
            break
        elif brackets[idx-1] == '[':
            ans += temp
        stk.pop()
        temp //= 3

if stk: # 예외처리 잊지말기
    print(0)
else:
    print(ans)