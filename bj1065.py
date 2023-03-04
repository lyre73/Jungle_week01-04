import sys

def isHan(num):
    digits = str(num)
    # print(digits)
    diff = 0
    for i in range(len(digits)-1):
        if i == 0:
            diff = int(digits[i]) - int(digits[i+1])
            continue
        elif int(digits[i]) - int(digits[i+1]) != diff:
            return False
    return True
    
N = int(sys.stdin.readline())
cnt = 0
for i in range(N):
    if isHan(i+1):
        cnt += 1
print(cnt)