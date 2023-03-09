N = int(input())
W = [[] for _ in range(N)]
global flag
flag = [False] + [True for _ in range(N-1)]
global min_wage
min_wage = float('inf')

for i in range(N):
    W[i] = list(map(int, input().split()))

def move(now, wage):
    global min_wage
    global flag
    # print(f'now = {now}, wage = {wage}')
    if True not in flag and W[now][0]:
        wage += W[now][0]
        print(f"{now} to {0}, wage = {wage}.\nI'm back!")
        if min_wage > wage: min_wage = wage
        return 0
    else:
        for i in range(N):
            if flag[i]:
                if W[now][i] != 0:
                    flag[i] = False
                    print(f'{now} to {i}, wage = {wage}')
                    move(i, wage + W[now][i])
                    flag[i] = True
move(0, 0)
print(min_wage)