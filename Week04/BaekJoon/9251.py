# # LCS
# # top-down 시간초과
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# str1 = input().rstrip()
# str2 = input().rstrip()

# dp = [[None] * len(str2) for _ in range(len(str1))]

# def LCS(idx1, idx2):
#     if idx1 == -1 or idx2 == -1: # 문자열 범위 밖이므로 LCS 존재 불가
#         return 0

#     if dp[idx1][idx2]: ## is not None
#         return dp[idx1][idx2]
    
#     if str1[idx1] == str2[idx2]:
#         dp[idx1][idx2] = LCS(idx1 - 1, idx2 - 1) + 1
#     else:
#         dp[idx1][idx2] = max(LCS(idx1 - 1, idx2), LCS(idx1, idx2-1)) # taking the maximum LCS found so far either by ignoring the current character in string 1 or string 2.
#     return dp[idx1][idx2]

# print(LCS(len(str1) -1, len(str2) -1))


# LCS
# bottom-up
import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)] # 0 - based

for idx1 in range(1, len(str1) + 1):
    for idx2 in range(1, len(str2) + 1):
        if str1[idx1 - 1] == str2[idx2 - 1]:
            dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1] + 1
        else:
            dp[idx1][idx2] = max(dp[idx1][idx2 - 1], dp[idx1 - 1][idx2])

print(dp[-1][-1])