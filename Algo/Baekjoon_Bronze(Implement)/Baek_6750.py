import sys

title = sys.stdin.readline().strip()
word_list = {
    "I", "O", "S", "H", "Z", "X", "N"
}
result = True

for i in range(len(title)):
    if title[i] not in word_list:
        result = False
        break

if result:
    print("YES")
else:
    print("NO")