# 요세푸스 문제 0
from collections import deque
import sys
input = sys.stdin.readline

def josephus():
    N, K = map(int, input().split())
    queue = deque(range(1, N+1))

    print('<', end='')
    while len(queue) > 1:
        # print(queue)
        queue.rotate(-K+1)
        print(queue.popleft(), end=', ')
        # print(queue)
    print(queue.popleft(), end='>\n')
josephus()