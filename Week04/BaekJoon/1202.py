# 보석 도둑
import sys, bisect
input = sys.stdin.readline

N, K = map(int, input().split())
gems = []
for _ in range(N):
    gems.append(tuple(map(int, input().split())))
gems.sort(key=lambda x: x[1], reverse=True)
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()

ans = 0
for gem in gems:
    if not bags:
        break
    else:
        weight, val = gem
        idx = bisect.bisect_left(bags, weight)
        if idx < len(bags):
            del(bags[idx]) # 이게 문제인 것 같은데 우선순위 큐로 어떻게 안 될까?
            ans += val
print(ans)