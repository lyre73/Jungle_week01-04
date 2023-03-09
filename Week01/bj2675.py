T = int(input())

for i in range(T):
    R, S = input().split()
    for letter in S:
        print(letter*int(R), end='')
    print()