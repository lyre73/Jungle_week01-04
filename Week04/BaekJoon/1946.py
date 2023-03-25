# 신입 사원
# chatGPT logic
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    applicants = []
    for _ in range(N):
        applicants.append(tuple(map(int, input().split())))
    applicants.sort()

    hired = 0
    best_interview = N + 1
    for _, interview in applicants:
        if interview < best_interview:
            hired += 1
            best_interview = interview
    print(hired)