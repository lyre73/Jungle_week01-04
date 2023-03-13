import heapq, sys
input = sys.stdin.readline

def cards():
    if int(input()) == 1:
        return print(0)
    heap = [int(i) for i in sys.stdin.readlines()]
    heapq.heapify(heap)
    temp = 0
    # print(heap)
    while len(heap) >= 2:
        cal = heapq.heappop(heap) + heapq.heappop(heap)
        heapq.heappush(heap, cal)
        temp += cal
        # print(heap, temp)
    print(temp)
cards()