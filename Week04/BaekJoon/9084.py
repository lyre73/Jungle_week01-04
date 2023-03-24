# 동전
import sys
input = sys.stdin.readline

def cal_coins():
    int(input())
    coins = tuple(map(int, input().split()))
    M = int(input())

    ans = [0] * (M + 1)
    ans[0] = 1 # 0원일 때의 경우의 수 만들어주기!!

    for coin in coins:
        for i in range(coin, M + 1):
            # if 0 <= i - coin <= M: # 0 포함하기!! # 근데 어차피 범위를 저렇게 정해서 필요없었겠다
            ans[i] += ans[i - coin]
    return ans[M]

for _ in range(int(input())):
    print(cal_coins())