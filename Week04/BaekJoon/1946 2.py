# 신입사원
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(N)]
    applicants.sort()
    employ = 0
    max_interview = 100001
    for applicant in applicants:
        if applicant[1] < max_interview:
            employ += 1
            max_interview = applicant[1]
    print(employ)