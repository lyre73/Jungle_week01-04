from __future__ import annotations

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key, value, left: Node = None, right: Node = None):
        """생성자(constructor)"""
        self.key = key # 키
        self.value = value # 값
        self.left = left # 왼쪽 포인터
        self.right = right # 오른쪽 포인터

class BinarySearchTree:
    """이진 검색 트리"""

    def __init__(self):
        """초기화"""
        self.root = None # 루트
    
    def search(self, key):
        """키가 key인 노드를 검색"""
        p = self.root # 루트에 주목, 포인터
        while True:
            if p is None: # 더 이상 진행할 수 없으면
                return None
            if key == p.key: # key와 노드 p의 키가 같으면
                return p.value # 검색 성공
            elif key < p.key: # key 쪽이 작으면
                p = p.left # 왼쪽 서브트리에서 검색
            else: # key 쪽이 크면
                p = p.right # 오른쪽 서브트리에서 검색
    
    def add(self, key, value):
        """키가 key이고 값이 value인 노드를 삽입"""

        def add_node(node, key, value):
            """node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽임"""
            if key == node.key:
                return False # key가 이진 검색 트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
