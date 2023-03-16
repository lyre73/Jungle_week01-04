# Moo 게임
import sys
input = sys.stdin.readline

memo = [None] * 29
global N
N = int(input())
if N == 1:
    print('m'), exit()
elif N <= 3:
    print('o'), exit()

def check(k):
    global N
    if N == 1:
            print('m'), exit()
    elif N <= 3:
            print('o'), exit()

    if N > memo[k-1] + k + 3:
        N -= memo[k-1] + k + 3
        check(k-1)
    elif N > memo[k-1]:
        if N - memo[k-1] == 1:
            print('m'), exit()
        else:
            print('o'), exit()
    else:
        check(k-1)

def moo(k):
    if memo[k]:
        global N
        if N <= memo[k]: # 처음으로 포함
            check(k)
        return memo[k]
    
    if k == 0:
        memo[0] = 3
        return 3
    else:
        memo[k] = moo(k-1) * 2 + (k + 3)
        return moo(k-1) * 2 + (k + 3)
moo(28)