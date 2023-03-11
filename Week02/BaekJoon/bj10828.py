# 스택

from collections import deque
import sys
input = sys.stdin.readline

class Stack:
    """고정 길이 스택 클래스(collections.deque)를 사용"""
    def __init__(self, maxlen: int = 256) -> None:
        """스택 초기화"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 개수를 반환"""
        return len(self.__stk)
    
    def is_empty(self) -> bool:
        """스택이 비어 있는지 판단"""
        return not self.__stk
    
    def push(self, value: int) -> None:
        """스택에 value를 푸시"""
        self.__stk.append(value)

    def pop(self) -> int:
        """스택에서 데이터를 팝"""
        if self.is_empty():
            return -1
        else:
            return self.__stk.pop()
    
    def peek(self) -> int:
        """스택에서 데이터를 피크"""
        if self.is_empty():
            return -1
        else:
            return self.__stk[-1]
    
N = int(input())
stk = Stack(N)
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        stk.push(int(command[1]))
    elif command[0] == 'pop':
        print(stk.pop())
    elif command[0] == 'size':
        print(len(stk))
    elif command[0] == 'empty':
        if stk.is_empty():
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        print(stk.peek())