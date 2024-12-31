import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    words.append(sys.stdin.readline().strip())

m = int(sys.stdin.readline())
candidate = []

# 중복 단어 제외
for _ in range(m):
    tmp = sys.stdin.readline().strip()

    if tmp not in words:
        candidate.append(tmp)

if n == 1:
    print(candidate[0])
else:
    # "?" 앞뒤 단어 체크
    before = ""
    after = ""

    if words.index("?") - 1 >= 0:
        before = words[words.index("?") - 1]

    if words.index("?") + 1 < len(words):
        after = words[words.index("?") + 1]

    # 이전 단어와 다음 단어 자리 확인
    for i in range(len(candidate)):
        if before != "" and candidate[i][0] == before[-1] and after != "" and candidate[i][-1] == after[0]:
            print(candidate[i])
            break
        elif before == "" and after != "" and candidate[i][-1] == after[0]:
            print(candidate[i])
            break
        elif before != "" and candidate[i][0] == before[-1] and after == "":
            print(candidate[i])
            break

# 다른 사람 풀이
# n = int(input())
# record = [input() for _ in range(n)]
# m = int(input())
# words = [input() for _ in range(m)]
#
# if n == 1:
#     print(words[0])
# elif record[0] == "?":
#     for word in words:
#         if word not in record and word[-1] == record[1][0]:
#             print(word)
#             break
# elif record[-1] == "?":
#     for word in words:
#         if word not in record and word[0] == record[-2][-1]:
#             print(word)
#             break
# else:
#     idx = record.index("?")
#     for word in words:
#         if word not in record and word[0] == record[idx - 1][-1] and word[-1] == record[idx + 1][0]:
#             print(word)
#             break