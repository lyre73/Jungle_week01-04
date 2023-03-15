import sys
input = sys.stdin.readline

def pseudo():
    N = int(input())
    data = list(map(int, input().split()))
    print(sum(data)/N/max(data)*100)
pseudo()