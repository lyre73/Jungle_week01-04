# import math
# import sys

# def isPrime(num):
#     if num == 1:
#         return False
#     elif num == 2 or num == 3:
#         return True
#     else:
#         for i in range(2, int(math.sqrt(num))+1):
#             if num % i == 0:
#                 return False
#             if i == int(math.sqrt(num)):
#                 return True
            
# T = int(sys.stdin.readline())

# for i in range(T):
#     n = int(sys.stdin.readline())
#     for j in range((n//2),1,-1):
#         if isPrime(j) and isPrime(n-j):
#             print(j, n-j)
#             break

import math
import sys

def isPrime(num):
    if num <= 3:
        if num < 2:
            return False
        return True
    else:
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                return False
    return True
            
T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    for j in range((n//2),1,-1):
        if isPrime(j) and isPrime(n-j):
            print(j, n-j)
            break