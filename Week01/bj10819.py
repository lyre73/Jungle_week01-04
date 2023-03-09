N = int(input())
A = list(map(int, input().split()))

global maximum
maximum = 0

def rearrange(nums: list, r):
    temp = []
    if r <= 1:
        return [nums]
    else:
        for idx in range(len(nums)):
            # 반환받은 리스트 안의 각각의 요소 앞에 nums[idx]를 삽입
            temp += [[nums[idx]] + i for i in rearrange(nums[:idx]+nums[idx+1:], r-1)]
        return temp
    
def cal(arr):
    global maximum
    for item in arr:
        temp = 0
        for i in range(N-1):
            temp += abs(item[i] - item[i+1])
            if maximum < temp:
                maximum = temp
cal(rearrange(A, N))
print(maximum)