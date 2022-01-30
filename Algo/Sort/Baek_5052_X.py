# 트라이를 도전하였으나 실패
# import sys
#
# t = int(sys.stdin.readline())
#
# class TrieNode:
#     def __init__(self):
#         self.word = False
#         self.children = {}
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#         self.checkList = {}
#
#     #단어 삽입
#     def insert(self, word: str) -> None:
#         node = self.root
#         checkStr = ""
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#                 checkStr += char
#             node = node.children[char]
#
#         self.checkList[checkStr] = 0
#         node.word = True
#
#     #단어 존재 여부 판별
#     def search(self, word: str) -> bool:
#         node = self.root
#         checkStr = ""
#         for char in word:
#             if char not in node.children:
#                 if checkStr in self.checkList:
#                     return False
#                 else:
#                     return True
#             checkStr += char
#             node = node.children[char]
#
#         return node.word
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     trie = Trie()
#     nums = []
#     check = False
#
#     for i in range(n):
#         num = sys.stdin.readline().strip()
#         nums.append(num)
#
#     nums.sort()
#
#     for i in nums:
#         if trie.search(i):
#             trie.insert(i)
#         else:
#             check = True
#
#     if check:
#         print("NO")
#     else:
#         print("YES")

# 간단히 정렬로도 풀리는 문제였다....
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    nums = [sys.stdin.readline().strip() for _ in range(n)]
    nums.sort()
    check = True

    for i in range(len(nums)-1):
        length = len(nums[i])
        if nums[i] == nums[i+1][:length]:
            check = False
            break

    if check:
        print("YES")
    else:
        print("NO")