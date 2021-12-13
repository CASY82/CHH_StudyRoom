import sys
n = int(sys.stdin.readline())
word = []
remove_word = []

for _ in range(n):
    word.append(sys.stdin.readline().strip())

word.sort(key = len)

for i in range(len(word)):
    for j in range(i + 1, len(word)):
        if word[j].startswith(word[i]):
            remove_word.append(word[i])
            break

print(len(word) - len(remove_word))

#다른사람 풀이 참고
# import sys; pin = sys.stdin.readline
# n = int(pin())
# arr = sorted([pin().strip() for _ in range(n)])
# ans = n
# for i in range(n):
#     if i != n-1:
#         if arr[i] == arr[i+1][:len(arr[i])]:
#             ans -= 1
# print(ans)