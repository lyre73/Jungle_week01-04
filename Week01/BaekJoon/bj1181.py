# arr = [[] for _ in range(51)]
# N = int(input())

# for _ in range(N):
#     word = input()
#     if word not in arr[len(word)]:
#         arr[len(word)].append(word)
# for idx in range(1, 51):
#     if arr[idx]:
#         print(*sorted(arr[idx]),sep='\n')

import sys

arr = [[] for _ in range(51)]

for _ in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().strip()
    arr[len(word)].append(word)
for words in arr[1:]:
    if len(words):
        print(*sorted(set(words)),sep='\n')