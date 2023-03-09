cnt = 0
N, S = map(int, input().split())
nums = list(map(int, input().split()))

def subsequence(nums: list, r):
    temp = []
    if r <= 1:
        return [[i] for i in nums]
    else:
        for i in range(len(nums)):
            if len(nums[i+1:]) >= r-1:
                for item in subsequence(nums[i+1:], r-1):
                    temp.append([nums[i]] + item)
        return temp

for i in range(1, N+1):
    for item in subsequence(nums, i):
        if sum(item) == S:
            cnt += 1
print(cnt)