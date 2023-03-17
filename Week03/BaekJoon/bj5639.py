# # 이진 검색 트리
# import sys
# sys.setrecursionlimit(10**6)

# keys = list(map(int, sys.stdin.readlines()))

# def postorder(start, end): # 지금 볼 (서브)트리의 시작~ 끝 인덱스
#     if start > end:
#         return
    
#     root = keys[start]
#     mid_idx = end + 1 # 이 서브트리 안에 루트보다 큰 자식이 없을 경우, 다음 서브트리는 왼쪽에만 있다
#     for i in range(start + 1, end + 1): # start+1, start+2, ... end-1, end
#         if keys[i] > root:
#             mid_idx = i
#             break
#     postorder(start + 1, mid_idx - 1) #루트, 다음 서브트리 (루트 빼고) 사이
#     postorder(mid_idx, end) # 다음 서브트리의 루트부터 끝까지. 아까 루트보다 큰 자식이 없었다면 그냥 return됨
#     print(keys[start])

# postorder(0, len(keys)-1)


# 이진 검색 트리 다시 풀기(공부안하고 그냥 다시 풀어보기, 나의 것으로 만들어보기)
"""전위 순환이었으니까 각 서브트리의 루트보다 큰 값이 나오면 그게 오른쪽 자식=오른쪽 서브트리의 루트가 된다. (그 전까지는 다 왼쪽 자식이 루트인 트리)
값을 다 받아 저장한 다음, 자식이 더 없을 때까지 가장 작은 트리로 나눠가기, 인덱스 활용"""

import sys
sys.setrecursionlimit(10**6)

# 데이터 다 받아오기
nodes = list(map(int, sys.stdin.readlines()))

def postorder(start, end):
    if start > end: # start == end여도 문제 발생 X
        return
    root = nodes[start] # 여러 번 쓸 거니까 선언해주는 게 더 빠른 것 같음
    right_child = end + 1 # 오른쪽 자식이 없으면 서브트리 영역 밖으로 보내버리기
    for i in range(start+1, end+1): # 루트를 제외한 나머지 값 중에 루트보다 큰 값(오른쪽 자식)이 있는지 확인
        if nodes[i] > root:
            right_child = i
            break
    postorder(start+1, right_child-1) # 왼쪽 자식이 루트인 서브트리만 다시 보기
    postorder(right_child, end) # 오른쪽 자식이 루트인 서브트리만 다시 보기
    print(root) # 후위 순환이니까 루트 노드의 값은 마지막에 출력
postorder(0, len(nodes)-1) # 처음부터 끝까지