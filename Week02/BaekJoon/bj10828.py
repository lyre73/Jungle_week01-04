# # 스택

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
#         """스택에 쌓여 있는 데이터 개수를 반환"""
#         return len(self.__stk)
    
#     def is_empty(self) -> bool:
#         """스택이 비어 있는지 판단"""
#         return not self.__stk
    
#     def push(self, value: int) -> None:
#         """스택에 value를 푸시"""
#         self.__stk.append(value)

#     def pop(self) -> int:
#         """스택에서 데이터를 팝"""
#         if self.is_empty():
#             return -1
#         else:
#             return self.__stk.pop()
    
#     def peek(self) -> int:
#         """스택에서 데이터를 피크"""
#         if self.is_empty():
#             return -1
#         else:
#             return self.__stk[-1]
    
# N = int(input())
# stk = Stack(N)
# for _ in range(N):
#     command = input().split()
#     if command[0] == 'push':
#         stk.push(int(command[1]))
#     elif command[0] == 'pop':
#         print(stk.pop())
#     elif command[0] == 'size':
#         print(len(stk))
#     elif command[0] == 'empty':
#         if stk.is_empty():
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'top':
#         print(stk.peek())


# 스택
# 다시 풀어본 코드

# import sys
# input = sys.stdin.readline

# stack = []

# for _ in range(int(input())):
#     command = input().split()
#     if command[0] == 'push':
#         stack.append(int(command[1]))
#     elif command[0] == 'pop':
#         if stack:
#             print(stack.pop())
#         else:
#             print(-1)
#     elif command[0] == 'size':
#         print(len(stack))
#     elif command[0] == 'empty':
#         if stack:
#             print(0)
#         else:
#             print(1)
#     else:
#         if stack:
#             print(stack[-1])
#         else:
#             print(-1)


# # 스택
# # 백준 상위권 보고 풀었음

import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    command = input().rstrip()
    if command == 'pop': print(stack.pop() if stack else -1)
    elif command == 'size': print(len(stack))
    elif command == 'empty': print(+(not stack)) # 와 +- boolean은 바로 출력되는구나
    elif command == 'top': print(stack[-1] if stack else -1)
    else: # 와 숫자는 이것만 필요하니까 int(x) 안 해도 되네... 근데 하는 게 빠르네
        _, x = command.split()
        stack.append(int(x))


# 스택
# 백준 상위권 보고 풀었음 + 다른 상위권 참고

# import sys
# input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    command = input().rstrip()
    if command == 'pop': print(stack.pop() if stack else -1)
    elif command == 'size': print(len(stack))
    elif command == 'empty': print(+(not stack)) # 와 +- boolean은 바로 출력되는구나
    elif command == 'top': print(stack[-1] if stack else -1)
    else: # 와 숫자는 이것만 필요하니까 int(x) 안 해도 되네... 근데 하는 게 빠르네
        stack.append(command[5:])



# 스택
# 백준 상위권 보고 match-case 문 사용해봤는데 시간 더 늘었음

# import sys
# input = sys.stdin.readline

# stack = []

# for _ in range(int(input())):
#     command = input().rstrip()
#     match command:
#         case 'pop': print(stack.pop() if stack else -1)
#         case 'size': print(len(stack))
#         case 'empty': print(0 if stack else 1)
#         case 'top': print(stack[-1] if stack else -1)
#         case _:
#             _, x = command.split()
#             stack.append(int(x))