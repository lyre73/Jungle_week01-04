# 카드2
# 10828 스택 참고
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    queue = deque(range(1, N+1))
    if N == 1:
        return print(1)

    while len(queue) > 1:
        queue.popleft()
        queue.rotate(-1)
    print(queue[0])
sol()