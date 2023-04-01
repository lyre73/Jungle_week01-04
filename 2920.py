notes = tuple(map(int, input().split()))
if notes == tuple(range(1, 9)):
    print("ascending")
elif notes == tuple(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")