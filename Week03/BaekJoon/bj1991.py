# 트리 순회
import sys
input = sys.stdin.readline

tree = [[] for _ in range(26)]
for _ in range(int(input())):
    key, left, right = map(ord, input().split()) # key = ord(value), idx = key - 65
    if left == 46:
        left = None
    if right == 46:
        right = None
    tree[key - 65] = ([key, left, right])

def preorder(node):
    print(chr(node[0]), end='')
    if node[1]:
        preorder(tree[node[1]-65])
    if node[2]:
        preorder(tree[node[2]-65])
preorder(tree[0])
print()

def inorder(node):
    if node[1]:
        inorder(tree[node[1]-65])
    print(chr(node[0]), end='')
    if node[2]:
        inorder(tree[node[2]-65])
inorder(tree[0])
print()

def postorder(node):
    if node[1]:
        postorder(tree[node[1]-65])
    if node[2]:
        postorder(tree[node[2]-65])
    print(chr(node[0]), end='')
postorder(tree[0])
print()