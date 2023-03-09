import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.read().strip().split('\n')))

print(*sorted(arr), sep='\n')