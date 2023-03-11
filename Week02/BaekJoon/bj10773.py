# # 제로

# from collections import deque
# import sys
# input = sys.stdin.readline

# class Stack:
#     """고정 길이 스택 클래스(collections.deque)를 사용"""
#     def __init__(self, maxlen: int = 256) -> None:
#         """스택 초기화"""
#         self.capacity = maxlen
#         self.__stk = deque([], maxlen)

#     def __len__(self) -> int:
#         return len(self.__stk)
    
#     def push(self, value: int) -> None:
#         """스택에 value를 푸시"""
#         self.__stk.append(value)

#     def pop(self) -> None:
#         """스택에서 데이터를 팝"""
#         self.__stk.pop()

#     def stksum(self) -> int:
#         sum = 0
#         for i in range(len(self)):
#             sum += self.__stk[i]
#         return sum
    
# K = int(input())
# stk = Stack(K)
# for _ in range(K):
#     command = int(input())
#     if command:
#         stk.push(command)
#     else:
#         stk.pop()
# print(stk.stksum())


# 제로
# 다시 풀어보기

import sys
input = sys.stdin.readline

def num():
    stk = []
    for _ in range(int(input())):
        n = int(input())
        if n:
            stk.append(n)
        else:
            stk.pop()
    print(sum(stk))
num() # 이렇게 함수 안에 묶고 다시 호출하는 건 다른 백준 답 보고 한 건데 꽤 빨라짐 왜일까?