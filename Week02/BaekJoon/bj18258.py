# # 큐 2
# # 10828 스택 참고
# from collections import deque
# import sys
# input = sys.stdin.readline

# def sol():
#     queue = deque()

#     for _ in range(int(input())):
#         command = input().rstrip()
#         if command == 'pop': print(queue.popleft() if queue else -1)
#         elif command == 'size': print(len(queue))
#         elif command == 'empty': print(+(not queue))
#         elif command == 'front': print(queue[0] if queue else -1)
#         elif command == 'back': print(queue[-1] if queue else -1)
#         else:
#             _, x = command.split()
#             queue.append(int(x))
# sol()


# 큐 2
# 백준 답 참고
from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

def sol():
    queue = deque()
    ans = []

    for _ in range(int(input())):
        command = input().rstrip()
        if command == 'pop': ans.append(queue.popleft() if queue else '-1')
        elif command == 'size': ans.append(str(len(queue)))
        elif command == 'empty': ans.append(str(+(not queue)))
        elif command == 'front': ans.append(queue[0] if queue else '-1')
        elif command == 'back': ans.append(queue[-1] if queue else '-1')
        else:
            _, x = command.split()
            queue.append(x)
    print('\n'.join(ans)) # 와 대단하다 출력에도 시간 걸리니까 그냥 다 모았다가 한번에 출력하네
sol()