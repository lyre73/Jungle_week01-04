import sys, heapq
input = sys.stdin.readline

def doubleQ():
    Q = []
    for _ in range(int(input())):
        for _ in range(int(input())):
            command = input()
            if command[0] == 'I':
                heapq.heappush(Q, int(command[2:]))
            elif Q:
                if command [2] == '-':
                    heapq.heappop(Q)
                else:
                    heapq._heapify_max(Q)
                    heapq.heappop(Q)
                    heapq.heapify(Q)
        if Q: print(max(Q), Q[0])
        else: print('EMPTY')
doubleQ()