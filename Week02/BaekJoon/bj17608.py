# 막대기

from collections import deque
import sys
input = sys.stdin.readline

class Stack:
    """고정 길이 스택 클래스(collections.deque)를 사용"""
    def Empty(Exception):
        """비어 있는 스택에 팝 또는 피크할 때 내보내는 예외 처리"""
        pass

    def __init__(self, maxlen: int = 256) -> None:
        """스택 초기화"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self):
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
            raise self.Empty()
        else:
            return self.__stk.pop()
        
    def peek(self) -> int:
        if self.is_empty():
            raise self.Empty()
        else:
            return self.__stk[-1]

    def clear(self):
        """스택을 비움"""
        self.__stk.clear()
        
N = int(input())
stk = Stack(N)
for _ in range(N):
    stick = int(input())
    while True:
        try:
            if stick >= stk.peek():
                stk.pop()
            else:
                stk.push()
                break
        except:
            stk.push(stick)
            break
print(len(stk))