# # 탑
# """탑 높이랑 번호를 받아서 튜플로 모아 저장한 다음, 앞에 자기보다 작은 탑 있으면 없애고 없애고... 자기보다 큰 탑 나오면 탑 번호 출력, 자기 푸시"""
# import sys
# input = sys.stdin.readline

# N = int(input())
# stack = [] # (탑 높이, 탑 번호) 형태로 저장
# i = 0 # 탑 번호를 저장할 변수

# for tower in map(int, input().split()):
#     i += 1 # 탑 번호 증가
#     while stack:
#         if stack[-1][0] < tower:
#             stack.pop()
#         else: # 앞에 자기보다 큰 탑을 발견!
#             print(stack[-1][1], end=' ')
#             break
#     else: # 스택이 비어있으면(앞에 자기보다 큰 탑이 하나도 없음)
#         print(0, end=' ')

#     stack.append((tower, i))


# 탑
# 백준 남의 답 거의 베낌...
# 높이가 아니라 번호만 저장, 인덱스 적극적 사용(나는 번호랑 높이를 둘 다 저장했었음)
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    stack = [] # 탑 번호만 저장
    goto = [0] * N # 탑마다 어디로 가는지만 0으로 초기화
    towers = list(map(int, input().split())) # 전체 탑 높이 데이터

    for i in range(N): # 탑 번호마다
        while stack and towers[stack[-1]] < towers[i]: # 스택이 비어있지 않으며 지금 (가려지지 않은)가장 오른쪽 탑이 지금 보는 탑보다 더 낮은 동안
                stack.pop() # 더 낮은 탑들을 지운다
        if stack: # 스택에 뭔가 남아있으면
             goto[i] = stack[-1] + 1 # 이 탑은 지금 (가려지지 않은)가장 오른쪽 탑으로 간다
        # 뭐가 안 남아있으면(얘가 제일 높은 거면) goto[i]는 갱신하지 않아서 그대로 0이다
        stack.append(i) # 현재 (가려지지 않은) 탑 번호에 자기 번호를 더함

    print(' '.join(map(str, goto)))
sol()