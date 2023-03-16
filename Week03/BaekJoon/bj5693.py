# 이진 검색 트리
import sys
sys.setrecursionlimit(10**6)

keys = list(map(int, sys.stdin.readlines()))

def postorder(start, end): # 지금 볼 (서브)트리의 시작~ 끝 인덱스
    if start > end:
        return
    
    root = keys[start]
    mid_idx = end + 1 # 이 서브트리 안에 루트보다 큰 자식이 없을 경우, 다음 서브트리는 왼쪽에만 있다
    for i in range(start + 1, end + 1): # start+1, start+2, ... end-1, end
        if keys[i] > root:
            mid_idx = i
            break
    postorder(start + 1, mid_idx - 1) #루트, 다음 서브트리 (루트 빼고) 사이
    postorder(mid_idx, end) # 다음 서브트리의 루트부터 끝까지. 아까 루트보다 큰 자식이 없었다면 그냥 return됨
    print(keys[start])

postorder(0, len(keys)-1)