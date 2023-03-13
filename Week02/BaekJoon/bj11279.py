# # 최대 힙
# import heapq, sys
# input = sys.stdin.readline

# heap = []

# for _ in range(int(input())):
#     num = int(input())
#     if num:
#         heapq.heappush(heap, (-num, num))
#     elif heap:
#         print(heapq.heappop(heap)[1])
#     else:
#         print(0)




# 최대 힙
# 참고
import heapq, sys
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    num = int(input())
    if num:
        heapq.heappush(heap, -num)
    elif heap:
        print(-heapq.heappop(heap))
    else:
        print(0)




# # 최대 힙
# # PriorityQueue를 썼더니 더 느림
# from queue import PriorityQueue
# import sys
# input = sys.stdin.readline

# queue = PriorityQueue()

# for _ in range(int(input())):
#     num = int(input())
#     if num:
#         queue.put((-num, num))
#     elif queue.empty():
#         print(0)
#     else:
#         print(queue.get()[1])