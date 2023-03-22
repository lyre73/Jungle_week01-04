# 숨바꼭질
import sys, collections
input = sys.stdin.readline

def hide_n_seek():
    N, K = map(int, input().split())

    Q = collections.deque([N])
    time = [-1] * 100001
    time[N] = 0

    while Q:
        u = Q.popleft()
        for next_place in [u - 1, u + 1, 2 * u]:
            if 0 <= next_place <= 100000 and time[next_place] == -1:
                time[next_place] = time[u] + 1
                Q.append(next_place)
            if next_place == K:
                return print(time[next_place])
hide_n_seek()