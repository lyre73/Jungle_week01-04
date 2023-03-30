# 연속합
# 내 코드 아님
import sys
input = sys.stdin.readline

n = int(input())
data = tuple(map(int, input().split()))

ans = [0]
for i in range(n):
    ans.append(max(ans[-1] + data[i], data[i]))
print(max(ans[1:]))
# print(ans)