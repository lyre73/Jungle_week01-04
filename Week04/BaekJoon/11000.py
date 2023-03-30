# 강의실 배정
import sys, heapq
input = sys.stdin.readline

N = int(input())
lectures = []
for _ in range(N):
    lectures.append(tuple(map(int, input().split())))
lectures.sort()

# 종료 시간 기준으로 우선순위 큐에 넣어줌
room = [0]
for start, end in lectures:
    if start >= room[0]:
        heapq.heapreplace(room, end)
    else:
        heapq.heappush(room, end)
print(len(room))