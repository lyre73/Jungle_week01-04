# def hanoi(tower, now, to, empty):
#     if tower < 1:
#         return
#     else:
#         hanoi(tower-1, now, empty, to)
#         print(now, to)
#         hanoi(tower-1, empty, to, now)

# N = int(input())
# print(2**N-1)
# if(N <= 20):
#     hanoi(N, 1, 3, 2)

# # hanoi(4, 1, 3, 2)

# """
# An = An-1 * 2 + 1
# An - 1 = An-1 * 2
# """

# another way
def hanoi(tower, now, to, spare):
    if tower == 1:
        print(now, to)
        return
    else:
        hanoi(tower-1, now, spare, to)
        print(now, to)
        hanoi(tower-1, spare, to, now)

N = int(input())
print((2 ** N)-1)
if(N <= 20):
    hanoi(N, 1, 3, 2)

# # aaand what if you don't use 'spare'? hmm (-4ms)
# def hanoi(tower, now, to):
#     if tower == 1:
#         print(now, to)
#         return
#     else:
#         hanoi(tower-1, now, 6 - now - to)
#         print(now, to)
#         hanoi(tower-1, 6 - now - to, to)

# N = int(input())
# print((2 ** N)-1)
# if(N <= 20):
#     hanoi(N, 1, 3)