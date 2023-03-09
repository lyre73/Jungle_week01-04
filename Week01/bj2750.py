# N = int(input())
# arranged = [float("-inf")]

# for _ in range(N):
#     num = int(input())
#     for i in range(len(arranged)):
#         if num <= arranged[i]:
#             arranged.insert(i, num)
#             break
#     else:
#         arranged.append(num)

# del arranged[0]

# for num in arranged:
#     print(num)


# another way with sort()
# N = int(input())
# arranged = []

# for _ in range(N):
#     arranged.append(int(input()))

# arranged.sort()

# for num in arranged:
#     print(num)


# another way with sorted()
N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

for num in sorted(arr):
    print(num)