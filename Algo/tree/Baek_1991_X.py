# 트리 순회 공부중
import sys

n = int(sys.stdin.readline().strip())
tree = {}

# 트리를 딕셔너리 형태로 만든다.
for _ in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

# 루트를 젤 앞에 찍는다.
def pre(root):
    if root != '.':
        print(root, end='')  # 루트 출력
        pre(tree[root][0])   # 왼쪽 순회 시작
        pre(tree[root][1])   # 오른쪽 순회 시작

# 루트가 가운데 찍힌다.
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # 왼쪽 순회
        print(root, end='')     # 루트 출력
        inorder(tree[root][1])  # 오른쪽 순회

# 루트가 제일 마지막에 찍힌다.
def post(root):
    if root != '.':
        post(tree[root][0])   # 왼쪽 순회 시작
        post(tree[root][1])   # 오른쪽 순회 시작
        print(root, end='')  # 루트 출력

pre('A')
print()
inorder('A')
print()
post('A')