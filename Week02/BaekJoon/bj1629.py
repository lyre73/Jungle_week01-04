"""곱하기 전에 각 단계마다 곱한거 % C"""

# 곱셈
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def mod(A, B, C):
    if B <= 1:
        return A % C
    if B % 2: # B is odd
        return ((mod(A, B//2, C) ** 2) * A) % C
    else: # B is even
        return (mod(A, B//2, C) ** 2) % C

print(mod(A, B, C))