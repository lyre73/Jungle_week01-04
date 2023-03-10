# # 색종이 만들기
# """각 사분면마다 상태 코드(혼합: -1, 흰색: 0, 파란색: 1)를 받아 네 칸을 비교.
# 색이 한 칸이라도 다르면 자르고, 새로 생기는 색종이(흰, 파) 개수 계산.
# 이 칸의 상태 코드 반환"""
# import sys, math
# input = sys.stdin.readline
# global white, blue
# white = blue = 0

# def check(k, r, c): # 종이 크기가 2^k, 시작 행 인덱스, 시작 열 인덱스
#     if k <= 0:
#         return color[r][c]
#     global white, blue
#     code = [check(k-1, r               , c),\
#             check(k-1, r               , c + (2 ** (k-1))),\
#             check(k-1, r + (2 ** (k-1)), c),\
#             check(k-1, r + (2 ** (k-1)), c + (2 ** (k-1)))]
#     if code[0] == code[1] == code[2] == code[3]:
#         if code[0] != -1:
#             return code[0]
#     else:
#         for i in range(4):
#             if code[i] == 0:
#                 white += 1
#             elif code[i] == 1:
#                 blue += 1
#         return -1

# N = int(input())
# color = [list(map(int, input().split())) for _ in range(N)]
# check(int(math.log2(N)), 0, 0)
# print(white, blue, sep='\n')

# 색종이 만들기
"""각 사분면마다 상태 코드(혼합: -1, 흰색: 0, 파란색: 1)를 받아 네 칸을 비교.
색이 한 칸이라도 다르면 자르고, 새로 생기는 색종이(흰, 파) 개수 계산.
이 칸의 상태 코드 반환"""
import sys
input = sys.stdin.readline
global white, blue
white = blue = 0

def check(side, r, c): # 한 변의 길이, 시작 행 인덱스, 시작 열 인덱스
    if side <= 1:
        return color[r][c]
    global white, blue
    half = side // 2
    code = [check(half, r       , c),\
            check(half, r       , c + half),\
            check(half, r + half, c),\
            check(half, r + half, c + half)]
    
    if code[0] == code[1] == code[2] == code[3]: # 네 사분면의 코드가 모두 같으면
        if code[0] != -1: # 그 코드가 혼합이 아닐 때(혼합뿐이면 안 봐도 됨)
            if side == N: # 변의 길이가 원래 종이 그대로면 전부 한 장이 된다
                if code[0] == 0:
                    white += 1
                elif code[0] == 1:
                    blue += 1
            return code[0]
    else: # 코드가 서로 달라서 종이를 잘라줘야 할 때
        for i in range(4): # 자른 종이가 새 색종이면 개수 더해주기
            if code[i] == 0:
                white += 1
            elif code[i] == 1:
                blue += 1
        return -1

N = int(input())
color = [list(map(int, input().split())) for _ in range(N)]
check(N, 0, 0)
print(white, blue, sep='\n')