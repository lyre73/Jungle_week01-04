# 철로
import heapq, sys
input = sys.stdin.readline

def railroad():
    people = int(input())
    data = [sorted(list(map(int, input().split()))) for _ in range(people)]
    data.sort(key=lambda x: x[1]) # 오른쪽 점을 기준으로 정렬
    dist = int(input())

    heap = []
    ans = 0

    for i in range(people): # 모든 선분을 돌면서
        if data[i][1] - dist <= data[i][0]: # 왼쪽 점이 기준(오른쪽 점 - 철로 길이)보다 오른쪽(철로 안에 들어가는 선분)
            heapq.heappush(heap, data[i][0]) # 힙에 왼쪽 점 추가
        while heap and heap[0] < data[i][1] - dist: # 힙의 최솟값(가장 왼쪽)이 기준보다 왼쪽(철로 안에 안 들어감)이면
            heapq.heappop(heap) # 그런 점은 다 빼기
        ans = max(ans, len(heap)) # 비교 후 큰 값으로 갱신
    print(ans)
railroad()