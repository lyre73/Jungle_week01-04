# 뒤집기
import sys
input = sys.stdin.readline

S = input().rstrip()
cnt = 0
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        cnt += 1
if S[0] != S[-1]:
    print(cnt // 2 + 1)
else:
    print(cnt // 2)



# 뒤집기
# 백준 상위권 답
import sys
input = sys.stdin.readline

S = input().rstrip()
print(max(S.count('01'), S.count('10')))