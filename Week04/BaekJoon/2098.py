# 외판원 순회
import sys
input = sys.stdin.readline

INF = float('inf')
N = int(input()) # 도시 N개, 0~N-1번 도시
weight = [list(map(int, input().split())) for _ in range(N)]
# print(weight)

dp = [[-1] * N for _ in range(1 << N)] # 0부터 2**N-1까지, 2 ** N개
# print(*dp, sep='\n')
dp[0][1] = 0 # visit_status = 0001

def TSP(visit_status, now): # now 도시부터, 남은 도시를 모두 방문하고 시작 도시를 가는 최소 비용을 리턴
    # print(f'visit_status:{visit_status}, now:{now}')
    if now != 0 and dp[visit_status][now] != -1:
        # print('case 1')
        return dp[visit_status][now]
    if visit_status == (1 << N) - 1: # 다 방문했으면
        # print('case2')
        if weight[now][0] == 0: # 여기서 시작 도시로 못 가는 경우, 유효하지 않은 경로
            dp[visit_status][now] = INF
        else:
            dp[visit_status][now] = weight[now][0]
        # print(f'dp[visit_status][now] = {dp[visit_status][now]}')
        return dp[visit_status][now]
    
    # print('case3')
    temp = INF
    for i in range(1, N): # 0은 출발 도시니까 1 ~ N-1번 도시까지
        # print(f'{bin(visit_status)} & {bin(1 << i)}')
        # print(not(visit_status & (1 << i)))
        if i != now and not (visit_status & (1 << i)): # 아직 i번 도시 안 갔으면
            if weight[now][i] == 0: # i번 도시 못 가면
                pass
            else:
                temp = min(temp, TSP(visit_status + (1 << i), i) + weight[now][i])
                # print(f'visit_status + (1 << i): {visit_status} + ({1 << i}), {temp}')
    dp[visit_status][now] = temp
    # print(temp)
    return temp
print(TSP(1, 0))

# print(*dp, sep='\n')

# print(0b1011 ^ (1 << 2))