import sys

words = sys.stdin.readline().strip()

length = len(words)
res = ""

for i in range(length):
    for j in range(i, length):
        if words[:i] != "" and words[i:j] != "" and words[j:] != "":
            if res == "":
                res = words[:i][::-1] + words[i:j][::-1] + words[j:][::-1]
            else:
                new = words[:i][::-1] + words[i:j][::-1] + words[j:][::-1]
                if new < res:
                    res = new

print(res)