# 힙 정렬 알고리즘 구현하기

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """힙 정렬"""

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right] 를 힙으로 만들기"""
        temp = a[left] # 루트의 값

        parent = left # 부모의 인덱스
        while parent < (right + 1) // 2: # 가장 마지막 요소의 부모 노드까지만
            cl = parent * 2 + 1 # 왼쪽 자식(의 인덱스)
            cr = parent * 2 + 2 # 오른쪽 자식(의 인덱스)
            child = cr if cr <= right and a[cr] > a[cl] else cl # 큰 자식의 인덱스
            if temp >= a[child]: # 더 큰 자식보다(모든 자식보다) 루트가 크면
                break
            a[parent] = a[child] # 부모의 값을 큰 자식의 값으로 변경
            parent = child # 큰 자식을 부모(주목하는 노드)로 재설정
        a[parent] = temp # 목적지에 루트의 값을 넣어준다
    
    n = len(a)

    for i in range((n - 1) // 2, -1, -1): # a[i] ~ a[n-1]을 힙으로 만들기 # i = (n-1)//2 , ... 0
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0] # 최댓값인 a[0]와 마지막 원소를 교환
        down_heap(a, 0, i - 1) # a[0] ~ a[i-1]을 힙으로 만들기


if __name__ == '__main__':
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = int(input())

    heap_sort(x)

    print(x)
