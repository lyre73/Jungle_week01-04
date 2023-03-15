# 랜선 자르기
import sys
input = sys.stdin.readline

def lan():
    K, N = map(int, input().split())
    data = list(map(int, sys.stdin.readlines()))
    
    start = 0
    end = 2147483647
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(K):
            cnt += data[i] // mid
        # print(f'mid = {mid}, cnt = {cnt}')
        if cnt < N:
            end = mid - 1
        else:
            start = mid + 1
    if cnt < N:
        print(mid - 1)
    else:
        print(mid)
lan()