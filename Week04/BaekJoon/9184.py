# 신나는 함수 실행
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def w(a, b, c):
    if (a, b, c) in dp:
        return dp[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        dp[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20:
        dp[(20, 20, 20)] = w(20, 20, 20)
        return dp[(20, 20, 20)]
    elif a < b < c:
        dp[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[(a, b, c)]

dp = {}
while True:
    a, b, c = map(int, input().split())
    if a != -1 or b != -1 or c != -1:
        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
    else:
        break