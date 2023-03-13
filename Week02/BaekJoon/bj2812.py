# # 크게 만들기
# """
# 앞에서부터 값 받아서 스택에 집어넣는데, 넣기 전에 앞에 있는 애가 더 작으면 없애기, 없앤 갯수 갱신, 다 없애면 넣기
# k개 없앨 때까지, 그리고 일단 받은 데이터 다 덤프한 다음 나머지는 입력받은 그대로 냅다 출력하기
# 주의: 예를 들어 2222222222나 22222222221같은 게 나오면 중간에 k개 처리 못함... K개만큼 못 지우고 N자리까지 다 받았으면... 어카지... 뒤에거를 지우고 출력하자"""

# from collections import deque
# import sys
# input = sys.stdin.readline

# class Stack:
#     """고정 길이 스택 클래스(collections.deque)를 사용"""

#     def __init__(self, maxlen: int = 256) -> None:
#         """스택 초기화"""
#         self.capacity = maxlen
#         self.__stk = deque([], maxlen)

#     def __len__(self):
#         """스택에 쌓여 있는 데이터 개수를 반환"""
#         return len(self.__stk)
    
#     def is_empty(self) -> bool:
#         """스택이 비어 있는지 판단"""
#         return not self.__stk
    
#     def push(self, value) -> None:
#         """스택에 value를 푸시"""
#         self.__stk.append(value)

#     def pop(self):
#         """스택에서 데이터를 팝"""
#         if self.is_empty():
#             raise self.Empty()
#         else:
#             return self.__stk.pop()
        
#     def peek(self):
#         if self.is_empty():
#             raise self.Empty()
#         else:
#             return self.__stk[-1]
        
#     def dump(self):
#         """스택 안에 있는 모든 데이터를 나열(바닥->꼭대기)해 반환"""
#         return ''.join(self.__stk)
        
# N, K = map(int, input().split())
# stk = Stack(N)
# while K > 0 and N > 0: # K개 다 지웠거나 마지막까지 보면 탈출
#     digit = sys.stdin.read(1) # 앞자리부터 훑기
#     N -= 1
#     # print(f'지금 읽은 숫자: {digit}, 앞으로 읽어올 숫자의 개수: {N}개, 앞으로 지울 숫자의 개수: {K}개')
#     if digit == '1': # 1이면 우선적으로 삭제
#         K -= 1
#     else: # 1이 아닌 숫자일 때
#         while not stk.is_empty() and K > 0: # 스택에 숫자가 있는 동안 + 지울 수가 남았으면
#             if digit > stk.peek(): # 지금 읽은 숫자보다 앞에 있는 숫자가 작으면
#                 stk.pop() # 앞에 있는 걸 없앰 
#                 K -= 1 # 지운 갯수 갱신
#             else: # 앞에 있는 숫자가 더 크면 탈출
#                 break
#         stk.push(digit) # 스택이 비어있거나 앞에 있는 숫자가 더 크면 새 숫자를 푸시
# else: # 다 읽었거나 다 지웠을 때
#     if K > 0: # 다 못 지우고 마지막까지 봤을 때
#         print(stk.dump()[:-K])
#     else: # 다 지웠는데 읽어올 게 남았을 때
#         print(stk.dump(), end='')
#         # print()
#         print(input().strip())

# # 4 > 41 > **7 > **77 > **772 > **77*5 > **


# # 크게 만들기
# # 다시 풀어보기
# """
# 앞에서부터 값 받아서 스택에 집어넣는데, 넣기 전에 앞에 있는 애가 더 작으면 없애기, 없앤 갯수 갱신, 다 없애면 넣기
# k개 없앨 때까지, 그리고 일단 받은 데이터 다 덤프한 다음 나머지는 입력받은 그대로 냅다 출력하기
# 주의: 예를 들어 2222222222나 22222222221같은 게 나오면 중간에 k개 처리 못함 K개만큼 못 지우고 N자리까지 다 받았으면 뒤를 지우고 출력하자"""

# import sys
# input = sys.stdin.readline

# def enlarge():
#     N, K = map(int, input().split())
#     stack = []

#     while K > 0 and N > 0: # 지울 게 남아있고 끝까지 다 읽었으면
#         digit = int(sys.stdin.read(1)) # 읽어오고
#         N -= 1 # 남은 숫자 개수 갱신
#         if digit == 0: # 0이면 우선적으로 삭제
#             K -= 1 # 지운 갯수 갱신
#         else: # 0이 아닌 숫자
#             while stack and stack[-1] < digit and K > 0: # 스택이 비지 않았고 스택 오른쪽 값보다 지금 값이 크고 지울 게 남았을 때
#                 stack.pop()
#                 K -= 1
#             stack.append(digit) # 남은 걸 다 지웠거나 지금 값이 더 작거나 지울 게 안 남았을 때
#     else:
#         if K > 0: # 다 못 지웠을 때(ex. 2222221)
#             print(''.join(map(str, stack[:-K])))
#         else: # 다 지우고 남은 거 있을 때
#             print(''.join(map(str, stack)) + input(), end='')
# enlarge()

# # 7 > 78 +> 8 > 89 +> 9 > 98 > 981 > 9811 > 98111 > 981111 > 9811110 +> 981111






# 크게 만들기
# 백준 상위권 참고
"""
앞에서부터 입력값 전부 받아서 스택에 집어넣는데, 넣기 전에 앞에 있는 애가 더 작으면 없애기, 없앤 갯수 갱신, 다 없애면 넣기
> k개 없앨 때까지. 다 받고 나면 뒤에서 지워야 할 만큼 더 빼고 출력
"""

import sys
input = sys.stdin.readline

def enlarge():
    N, K = map(int, input().split())
    stack = []
    cnt = 0 # K와 cnt를 분리한 이유: 마지막 출력 시 최대 길이(N-K)를 고정하기 위해서(K를 손대면 K가 0일 때 stack[:-K] 출력이 안 됨)

    for digit in input().rstrip():
        while stack and stack[-1] < digit and cnt < K:
            stack.pop()
            cnt += 1
        stack.append(digit)
        
    print(''.join(stack[:N-K]))
enlarge()

# 7 > 78 +> 8 > 89 +> 9 > 98 > 981 > 9811 > 98111 > 981111 > 9811110 +> 981111