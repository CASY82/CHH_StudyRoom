import sys

n, m = map(int, sys.stdin.readline().split())

prefix = set()
result = 0

for _ in range(n):
    word = sys.stdin.readline().strip()

    for i in range(len(word)+1):
        prefix.add(word[:i])

for _ in range(m):
    compare_word = sys.stdin.readline().strip()
    if compare_word in prefix:
        result += 1

print(result)

# 다른사람 풀이(trie 인것 같다)

# class N:
#     def __init__(self):
#         self.children={}
# class T:
#     def __init__(self):
#         self.root=N()
#     def push(self,w):
#         node=self.root
#         for c in w:
#             if c not in node.children:
#                 node.children[c]=N()
#             node=node.children[c]
#     def search(self,w):
#         node=self.root
#         for c in w:
#             if c not in node.children:
#                 return False
#             node=node.children[c]
#         return True
# n,m=map(int,input().split())
# r,c=T(),0
# for _ in range(n):
#     r.push(input())
# for _ in range(m):
#     if r.search(input()):
#         c+=1
# print(c)