# 그래프 수정
# 참고 https://velog.io/@whddn0221/백준-1432-그래프-수정-위상정렬-우선순위-큐-mrltwcp5
"""진출 차수가 작은 것부터 큰 수를 배정해 준다. 진출 차수가 같다면 노드 번호가 큰 것부터 준다. 사이클을 판별해서 있으면 -1을 출력한다."""
import sys, heapq
input = sys.stdin.readline

# 데이터 받기
N = int(input())
G = [[0 for _ in range(N + 1)]]
outdegree = [0] * N
new_seq = [0] * N
G = []

for i in range(N):
    temp = list(map(int, input().rstrip()))
    G.append(temp)
    outdegree[i] += temp.count(1)

# 큐 초기화
Q = []
for i in range(N - 1, -1, -1):
    if outdegree[i] == 0:
        heapq.heappush(Q, -i) # 최대 힙(큰 숫자부터 꺼내야 하니까)

num = N # N부터 1까지 새로 넣어줄 숫자(N을 직접 줄이면 당연히 큰일남)
while Q:
    idx = -heapq.heappop(Q)
    new_seq[idx] = num # 숫자 새로 넣어주기
    num -= 1 # 넣어줄 숫자 갱신
    for i in range(N):
        # 지금 팝한 노드로 들어오는 간선들 제거(연결된 노드의 진출 차수 제거)
        if G[i][idx] > 0:
            outdegree[i] -= 1
            if outdegree[i] == 0:
                heapq.heappush(Q, -i)
if new_seq.count(0) == 0:
    print(*new_seq, sep=' ')
else:
    print(-1)