# 괄호

from collections import deque
import sys
input = sys.stdin.readline

class Stack:
    class Empty(Exception):
        pass

    """고정 길이 스택 클래스(collections.deque)를 사용"""
    def __init__(self, maxlen: int = 256) -> None:
        """스택 초기화"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)
    
    def is_empty(self) -> bool:
        """스택이 비어 있는지 판단"""
        return not self.__stk
    
    def push(self, value: int) -> None:
        """스택에 value를 푸시"""
        self.__stk.append(value)

    def pop(self):
        """스택에서 데이터를 팝"""
        try:
            return self.__stk.pop()
        except:
            raise Stack.Empty
    
    def clear(self):
        """스택을 비움"""
        self.__stk.clear()
        
stk = Stack(50)
for _ in range(int(input())):
    stk.clear()
    for char in input().strip():
        if char == '(':
            stk.push(1)
        else:
            try:
                stk.pop()
            except:
                print('NO')
                break
    else:
        if stk.is_empty():
            print('YES')
        else:
            print('NO')