# # 트리 순회
# import sys
# input = sys.stdin.readline

# tree = [[] for _ in range(26)]
# for _ in range(int(input())):
#     key, left, right = map(ord, input().split()) # key = ord(value), idx = key - 65
#     if left == 46:
#         left = None
#     if right == 46:
#         right = None
#     tree[key - 65] = ([key, left, right])

# def preorder(node):
#     print(chr(node[0]), end='')
#     if node[1]:
#         preorder(tree[node[1]-65])
#     if node[2]:
#         preorder(tree[node[2]-65])
# preorder(tree[0])
# print()

# def inorder(node):
#     if node[1]:
#         inorder(tree[node[1]-65])
#     print(chr(node[0]), end='')
#     if node[2]:
#         inorder(tree[node[2]-65])
# inorder(tree[0])
# print()

# def postorder(node):
#     if node[1]:
#         postorder(tree[node[1]-65])
#     if node[2]:
#         postorder(tree[node[2]-65])
#     print(chr(node[0]), end='')
# postorder(tree[0])
# print()



# 트리 순회
# 각 노드를 딕셔너리로 입력받기(숫자가 아니니까 리스트 인덱스로 접근하려면 추가로 아스키코드 값 필요)
# cih831 코드 참고...했는데 속도 개선은 X. 그래도 가독성 향상
import sys
input = sys.stdin.readline

def preorder(key):
    if key == '.': # 판단하고 호출 X. 호출하고 나서 판단
        return
    print(key, end='')
    preorder(tree[key][0])
    preorder(tree[key][1])

def inorder(key):
    if key == '.': # 판단하고 호출 X. 호출하고 나서 판단
        return
    inorder(tree[key][0])
    print(key, end='')
    inorder(tree[key][1])

def postorder(key):
    if key == '.': # 판단하고 호출 X. 호출하고 나서 판단
        return
    postorder(tree[key][0])
    postorder(tree[key][1])
    print(key, end='')

tree = {} # 딕셔너리
for _ in range(int(input())):
    node, left, right = input().split()
    tree[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')