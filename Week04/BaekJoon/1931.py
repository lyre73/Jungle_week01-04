# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
schedule = []
for _ in range(N):
    start, end = map(int, input().split())
    schedule.append((end, start))
schedule.sort() # 자동으로 x[1]도 고려해줌
# schedule 에 (start, end) 순서로 넣었을 때
# schedule.sort(key=lambda x: x[0]) # 시작 시간 == 끝나는 시간일 수도 있으니까 끝나는 시간이 같다면 시작 시간 빠른 것부터 체크
# schedule.sort(key=lambda x: x[1])

ans = [0, 0] # 끝나는 시간, 회의 개수
for end, start in schedule:
    if start >= ans[0]:
        ans = [end, ans[1] + 1]
print(ans[1])