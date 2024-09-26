import sys

sentense = sys.stdin.readline().strip()
alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
cnt = [0 for _ in range(26)]

for i in range(len(sentense)):
    if sentense[i].upper() in alpha:
        cnt[alpha.index(sentense[i].upper())] += 1

for i in range(26):
    print("{0} | ".format(alpha[i]), end="")
    for _ in range(cnt[i]):
        print("*", end="")
    print()

# 다른 사람 풀이
# text = input().upper()
# alps = [0] * 26
# for t in text:
#     index = ord(t)
#     if 65 <= index <= 90:alps[index - 65] += 1
# for i in range(26):print(f'{chr(i + 65)} | {"*" * alps[i]}')