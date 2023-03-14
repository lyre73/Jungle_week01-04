# # 요세푸스 문제 0
# from collections import deque
# import sys
# input = sys.stdin.readline

# def josephus():
#     N, K = map(int, input().split())
#     queue = deque(range(1, N+1))

#     print('<', end='')
#     while len(queue) > 1:
#         # print(queue)
#         queue.rotate(-K+1)
#         print(queue.popleft(), end=', ')
#         # print(queue)
#     print(queue.popleft(), end='>\n')
# josephus()



# 요세푸스 문제 0
# 백준 상위권 답 확인
# 큐를 안 쓰는 게 더 빠르네...
import sys
input = sys.stdin.readline

def josephus():
    N, K = map(int, input().split())
    people = list(range(1, N+1))
    ans = []
    idx = 0

    while people:
        idx += K - 1
        idx %= len(people)
        ans.append(str(people.pop(idx)))
    print("<",", ".join(ans), ">", sep="")
josephus()