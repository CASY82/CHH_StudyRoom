import sys

word = list(sys.stdin.readline().strip())

word.sort()
tmp_set = list(set(word))

res_tmp = []

for i in range(len(tmp_set)):
    res_tmp.append((tmp_set[i], word.count(tmp_set[i])))

res_tmp.sort(key = lambda x:(-x[1], x[0]))
result = ""

for alp, cnt in res_tmp:
    for _ in range(cnt):
        result += alp

print(result)