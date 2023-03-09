# import sys

# N = int(sys.stdin.readline())
# arr = [0] * 10000
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     arr[num-1] += 1

# for idx in range(10000):
#     for _ in range(arr[idx]):
#         print(idx+1)

# wow used time half
import sys

N = int(sys.stdin.readline())
arr = [0] * 10001
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for idx in range(1, 10001):
    if arr[idx]:
        while arr[idx] > 1000:
            print((str(idx)+'\n')*1000,end='')
            arr[idx] -= 1000
        print((str(idx)+'\n')*arr[idx],end='')


# trying to use dict... and this is worse(use more memory and time)
# import sys

# N = int(sys.stdin.readline())
# arr = {}
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     if num in arr.keys():
#         arr[num] += 1
#     else:
#         arr[num] = 1
# for key in sorted(arr.keys()):
#     for _ in range(arr[key]):
#         print(key)