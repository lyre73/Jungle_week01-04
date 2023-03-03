nums = []
for i in range(9):
    nums.append(int(input()))

# nums = [int(i) for i in input().split()]

max_val = max(nums)
print(max_val, nums.index(max_val)+1, sep='\n')