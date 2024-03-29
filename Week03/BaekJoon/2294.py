# 동전 2
# DP
import sys
input = sys.stdin.readline

# 데이터 받기
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# 가격별 필요 동전 개수 초기화
dp = [10001] * (k + 1)
dp[0] = 0

# for i in range(1, k + 1):
#     for coin in coins:
#         dp[i] = min(dp[i], dp[i - coin] + 1)
for coin in coins: # 조심! 위 주석처럼 쓰면 IndexError 발생
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != 10001 else -1)





# 동전 2
# BFS
"""비교 없이 한 번만 방문해도 되나? 싶었는데 더 큰 값의 동전이 더 적은 개수로 빠르게 값을 키울 거니까 ㄱㅊ"""
import sys, collections
input = sys.stdin.readline

# 데이터 받기
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

Q = collections.deque([(0, 0)]) # 0원, 동전 0개
visited = [False] * (k + 1)

while Q:
    price, num_coins = Q.popleft()
    # visited[price] = True

    if price == k:
        print(num_coins)
        break

    for coin in coins:
        new_price = price + coin
        if new_price <= k and not visited[new_price]:
            visited[new_price] = True # 주의! 위 주석처럼 팝할 때 방문 갱신하면 중복 방문이 많아져서 시간초과 남!
            Q.append((new_price, num_coins + 1))
else:
    print(-1)




"""chatGPT code
from collections import deque

def min_coins_bfs(n, k, coins):
    visited = [False] * (k + 1)
    queue = deque([(0, 0)])  # (value, num_coins)

    while queue:
        value, num_coins = queue.popleft()
        
        if value == k:
            return num_coins
        
        for coin in coins:
            new_value = value + coin
            
            if 0 <= new_value <= k and not visited[new_value]:
                visited[new_value] = True
                queue.append((new_value, num_coins + 1))
    
    return -1

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

result = min_coins_bfs(n, k, coins)
print(result)
"""