def modified_nPr(nums, r):
    temp = []
    if r <= 1:
        return nums
    else:
        for idx in range(len(nums)):
            temp += [nums[idx] + i for i in set(modified_nPr(nums[:idx]+nums[idx+1:], r-1))]
        return temp

n = int(input())
k = int(input())
cards = []

for _ in range(n):
    cards.append(input())

print(len(set(modified_nPr(cards, k))))