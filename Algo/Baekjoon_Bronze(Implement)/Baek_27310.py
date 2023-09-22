import sys

imoji = sys.stdin.readline().strip()

full_length = len(imoji)
collon_cnt = imoji.count(":")
underbar_cnt = imoji.count("_")

print(full_length + collon_cnt + underbar_cnt * 5)