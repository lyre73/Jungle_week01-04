# 가운데를 말해요
import heapq, sys
input = sys.stdin.readline

leftheap = [float('inf')] # 최대 힙
rightheap = [float('inf')] # 최소 힙

for _ in range(int(input())):
    if len(leftheap) <= len(rightheap):
        heapq.heappush(leftheap, -int(input()))
    else:
        heapq.heappush(rightheap, int(input()))
    if -leftheap[0] > rightheap[0]:
        leftmax = -heapq.heappop(leftheap)
        rightmin = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -rightmin)
        heapq.heappush(rightheap, leftmax)
    print(-leftheap[0])