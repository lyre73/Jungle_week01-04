# # 구간 합 구하기 4
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# sequence = tuple(map(int, input().split()))
# data = []
# _max = 0

# for _ in range(M):
#     temp = tuple(map(int, input().split()))
#     data.append(temp)
#     _max = max(_max, temp[0], temp[1])

# DP = [0] * (N + 1)
# for i in range(1, _max + 1):
#     DP[i] = DP[i - 1] + sequence[i - 1]
# for datum in data:
#     i, j = datum
#     print(DP[j] - DP[i - 1])



# 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sequence = tuple(map(int, input().split()))

DP = [0] * (N + 1)
for i in range(1, N + 1):
    DP[i] = DP[i - 1] + sequence[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(DP[j] - DP[i - 1])