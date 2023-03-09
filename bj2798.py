# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# global nearM
# nearM = 0

# def black_jack(nums):
#     global nearM
#     for i in range(N-2):
#         for j in range(i+1, N-1):
#             for k in range(j+1, N):
#                 temp = nums[i] + nums[j] + nums[k]
#                 if temp == M:
#                     nearM = M
#                     break
#                 elif nearM < temp < M:
#                     nearM = temp

# black_jack(cards)
# print(nearM)

# 수를 내림차순 정렬해 각 분기마다 큰 수 -> 작은 수 순으로 계산해서, M보다 작은 수는 하나만 확인하고 break
N, M = map(int, input().split())
cards = sorted(list(map(int, input().split())), reverse=True)
nearM = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= M:
                if nearM < temp:
                    nearM = temp
                break

print(nearM)