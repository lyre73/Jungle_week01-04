# # N-Queen
N = int(input())

global cnt, flag_a, flag_b, flag_c
# pos = [None] * N
flag_a = [True] * N # 십자로 놓을 수 있는지
flag_b = [True] * (2 * N - 1) # / 방향으로 놓을 수 있는지
flag_c = [True] * (2 * N - 1) # \ 방향으로 놓을 수 있는지
cnt = 0

def set(N, row):
    global cnt, flag_a, flag_b, flag_c
    if N <= 6:
        for col in range(N):
            if flag_a[col] and flag_b[row + col] and flag_c[row - col + N - 1]:
                if row == N-1:
                    cnt += 1
                else:
                    flag_a[col] = flag_b[row + col] = flag_c[row - col + N - 1] = False
                    set(N, row+1)
                    flag_a[col] = flag_b[row + col] = flag_c[row - col + N - 1] = True
    else:
        ?

set(N, 0)
print(cnt)