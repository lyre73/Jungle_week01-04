# 뱀
from collections import deque
import sys
input = sys.stdin.readline

def dummy():
    N = int(input())
    K = int(input())
    mode = deque(['R', 'D', 'L', 'U'])
    time = 0
    apple = []
    for _ in range(K):
        apple.append(tuple(map(int, input().split())))
    snake = deque([(1, 1)])
    for _ in range(int(input())):
        t, rotate = input().split()
        t = int(t)
        if mode[0] == 'R':
            for _ in range(t - time):
                time += 1
                snake.append((snake[-1][0], snake[-1][1] + 1))
                if snake.count(snake[-1]) > 1 or snake[-1][1] > N:
                    return print(time)
                elif snake[-1] in apple:
                    apple.remove(snake[-1])
                else:
                    snake.popleft()
        elif mode[0] == 'L':
            for _ in range(t - time):
                time += 1
                snake.append((snake[-1][0], snake[-1][1] - 1))
                if snake.count(snake[-1]) > 1 or snake[-1][1] < 1:
                    return print(time)
                elif snake[-1] in apple:
                    apple.remove(snake[-1])
                else:
                    snake.popleft()
        elif mode[0] == 'D':
            for _ in range(t - time):
                time += 1
                snake.append((snake[-1][0] + 1, snake[-1][1]))
                if snake.count(snake[-1]) > 1 or snake[-1][0] > N:
                    return print(time)
                elif snake[-1] in apple:
                    apple.remove(snake[-1])
                else:
                    snake.popleft()
        else:
            for _ in range(t - time):
                time += 1
                snake.append((snake[-1][0] - 1, snake[-1][1]))
                if snake.count(snake[-1]) > 1 or snake[-1][0] < 1:
                    return print(time)
                elif snake[-1] in apple:
                    apple.remove(snake[-1])
                else:
                    snake.popleft()
        if rotate == 'D':
            mode.rotate(-1)
        else:
            mode.rotate(1)
    if mode[0] == 'R':
        while True:
            time += 1
            snake.append((snake[-1][0], snake[-1][1] + 1))
            if snake.count(snake[-1]) > 1 or snake[-1][1] > N:
                return print(time)
            elif snake[-1] in apple:
                apple.remove(snake[-1])
            else:
                snake.popleft()
    elif mode[0] == 'L':
        while True:
            time += 1
            snake.append((snake[-1][0], snake[-1][1] - 1))
            if snake.count(snake[-1]) > 1 or snake[-1][1] < 1:
                return print(time)
            elif snake[-1] in apple:
                apple.remove(snake[-1])
            else:
                snake.popleft()
    elif mode[0] == 'D':
        while True:
            time += 1
            snake.append((snake[-1][0] + 1, snake[-1][1]))
            if snake.count(snake[-1]) > 1 or snake[-1][0] > N:
                return print(time)
            elif snake[-1] in apple:
                apple.remove(snake[-1])
            else:
                snake.popleft()
    else:
        while True:
            time += 1
            snake.append((snake[-1][0] - 1, snake[-1][1]))
            if snake.count(snake[-1]) > 1 or snake[-1][0] < 1:
                return print(time)
            elif snake[-1] in apple:
                apple.remove(snake[-1])
            else:
                snake.popleft()
dummy()