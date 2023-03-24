# 계단 오르기
# 2차원 배열 DP
import sys
input = sys.stdin.readline

N = int(input())
scores = [0]
for _ in range(N):
    scores.append(int(input()))
# print(scores)

DP = [[0, 0] for _ in range(N + 1)] # 이 앞에 연속 0개 밟음, 연속 1개 밟음

for i in range(1, N + 1):
    DP[i][0] = max(DP[i-2][0], DP[i-2][1]) + scores[i]
    DP[i][1] = DP[i-1][0] + scores[i]
print(max(DP[-1][0], DP[-1][1]))



# 계단 오르기
# 1차원 배열 DP
import sys
input = sys.stdin.readline

N = int(input())
INF = float('inf')
scores = [0]
for _ in range(N):
    scores.append(int(input()))
if N <= 2:
    print(sum(scores))
elif N == 3:
    print(sum(scores) - min(scores[1], scores[2]))
else:
    DP = [INF] * N # D[i] = i번째 계단에 올라섰을 때 밟지 않을 계단의 합의 최솟값, i번째 계단은 밟지 않음 = i - 1은 밟아야 함, i-2 or i-3 중 하나는 밟아야 함
    for i in range(1, 4):
        DP[i] = scores[i] # 초기값 구하는 게 어렵네

    for i in range(4, N): # 마지막 계단은 고려 x
        DP[i] = min(DP[i - 2], DP[i - 3]) + scores[i] # 설명을 들으니까 그대로 점화식은 만들었음
    print(sum(scores) - min(DP[N-1], DP[N-2])) # 마지막 계단은 밟는다



# 계단 오르기
# 1차원 배열 DP 2
import sys
input = sys.stdin.readline

N = int(input())
scores = [0]
for _ in range(N):
    scores.append(int(input()))
DP = [0] * (N + 1) # i번째 계단에 올라섰을 때 점수 합의 최댓값, i번째 계단은 밟음 = max(d[i-2], d[i-3] + s[i-1]) + s[i]
if N <= 2:
    print(sum(scores[:N + 1]))
else:
    for i in range(1, 3):
        DP[i] = sum(scores[:i + 1])
    for i in range(3, N + 1):
        DP[i] = max(DP[i - 3] + scores[i - 1], DP[i - 2]) + scores[i]
    print(DP[N])