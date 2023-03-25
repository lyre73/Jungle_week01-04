# 카드 합체 놀이
import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
heapq.heapify(A)

for _ in range(m):
    a, b = heapq.heappop(A), heapq.heappop(A)
    heapq.heappush(A, a + b)
    heapq.heappush(A, a + b)
print(sum(A))