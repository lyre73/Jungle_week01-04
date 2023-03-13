# 큐 2
# 10828 스택 참고
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    queue = deque()

    for _ in range(int(input())):
        command = input().rstrip()
        if command == 'pop': print(queue.popleft() if queue else -1)
        elif command == 'size': print(len(queue))
        elif command == 'empty': print(+(not queue))
        elif command == 'front': print(queue[0] if queue else -1)
        elif command == 'back': print(queue[-1] if queue else -1)
        else:
            _, x = command.split()
            queue.append(int(x))
sol()