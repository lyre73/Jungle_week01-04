import math

input()
nums = map(int, input().split())
cnt = 0
for num in nums:
    if num == 1:
        continue
    elif num == 2 or num == 3:
        cnt += 1
        continue
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
            if i == int(math.sqrt(num)):
                cnt += 1
print(cnt)