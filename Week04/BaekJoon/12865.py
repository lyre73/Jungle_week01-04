# 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = [] # weight, value
for _ in range(N):
    data.append(tuple(map(int, input().split())))
# print(data)

dp = [0] * (K + 1)

# for i in range(1, K + 1):
#     temp = 0
#     for article in data: # article: 물건
#         weight, value = article
#         if 0 <= i - weight: # 0 포함!!!1
#             print(i, article, dp[i - weight])
#             temp = max(temp, dp[i - weight] + value)
#     dp[i] = temp

for article in data:
    weight, value = article
    for i in range(K, 0, -1):
        if i - weight >= 0:
            dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[K])

"""
The main difference is the order of the loops and how the dp table is updated.
In your code, you were iterating through the items for each weight limit,
which didn't ensure that you were considering the optimal choices for each item.
This approach can lead to double counting items or not counting some optimal choices.

In the corrected code, we iterate through the items first, and then through the weight limits in reverse order.
This way, we make sure that we only consider each item once,
and we guarantee that we are considering the optimal choices for each item while updating the dp table.

This change in the order of the loops and the direction of the inner loop ensures
that the algorithm correctly computes the maximum value that can be achieved within the given weight limit.
"""