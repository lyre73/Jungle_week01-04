# # 평범한 배낭
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# data = []
# for _ in range(N):
#     data.append(tuple(map(int, input().split())))

# dp = [0] * (K + 1)

# for article in data:
#     weight, value = article
#     for i in range(K, 0, -1):
#         if i - weight >= 0:
#             dp[i] = max(dp[i], dp[i - weight] + value)

# print(dp[K])

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

# 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
articles = []
dp = [0] * (K + 1)
for _ in range(N):
    articles.append(tuple(map(int, input().split())))

for article in articles:
    weight, value = article
    for i in range(K, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)
print(dp[-1])

"""
If we were to iterate through the weight limits from 1 to K (i.e., left-to-right),
we might end up using the same item multiple times. 
This is because, while updating dp[j], the value of dp[j - weight] might have already been updated 
using the same item in the current iteration. 
As a result, we might use the same item twice or even more, 
which violates the 0/1 knapsack constraint that each item can be used at most once.

To avoid this issue, we iterate through the weight limits in reverse order (K to 1). 
By doing this, we ensure that while updating dp[j], the value of dp[j - weight] is not influenced by the current item. 
In other words, the value of dp[j - weight] corresponds to 
the maximum value achievable with the previous items only, which guarantees that each item is used at most once.

In summary, iterating in reverse order helps maintain the constraint that each item can be used only once, 
ensuring the correctness of the algorithm for the 0/1 knapsack problem."""