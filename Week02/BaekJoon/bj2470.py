# 두 용액
import sys
input = sys.stdin.readline

N = int(input())
solution = sorted(list(map(int, input().split())))

left = 0
right = N-1
result = [float('inf'), left, right]
while left < right:
    mixture = solution[left] + solution[right]
    # print(f'sol.left = {solution[left]}, sol.right = {solution[right]}')
    if mixture == 0:
        result = [0, left, right]
        break
    elif mixture < 0:
        if abs(mixture) < abs(result[0]):
            result = [mixture, left, right]
        left += 1
    else:
        if abs(mixture) < abs(result[0]):
            result = [mixture, left, right]
        right -= 1
    # print(f'result[0] became {result[0]}')
print(solution[result[1]], solution[result[2]])