# 멀티탭 스케줄링
# 이미 사용이 끝났거나 가장 빠르게 사용이 끝날 것을 먼저 집어넣기
import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())


usage = [0] + list(map(int, input().split()))
data = [[[-101], i] for i in range(K + 1)] # data[i][0] : i번 전기용품의 사용 시점 리스트(-부호), data[i][1] : 전기용품 번호

for i in range(1, K + 1):
    data[usage[i]][0].insert(-1, -i)
        
# print(data)

Q = [data[usage[1]]]
cnt = 0

# 이 시점 뒤에 등장이 가장 늦은 것부터 뽑기
for i in range(2, K + 1):
    # 이 시점 뒤인 걸 갱신해주기
    for node in Q:
        while node[0][0] >= -i:
            node[0].pop(0)
    for j in range(1, K + 1):
        while data[j][0][0] >= -i:
            data[j][0].pop(0)
    heapq.heapify(Q)
    
    if data[usage[i]] not in Q:
        if len(Q) >= N:
            heapq.heappop(Q)
            cnt += 1
        heapq.heappush(Q, data[usage[i]])

print(cnt)