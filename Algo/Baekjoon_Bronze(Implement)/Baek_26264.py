import sys

n = int(sys.stdin.readline())

sentence = sys.stdin.readline().strip()

sec = "security"
data = "bigdata"

cnt = [0, 0]

cnt[0] = sentence.count(sec)
cnt[1] = sentence.count(data)

if cnt[0] > cnt[1]:
    print("security!")
elif cnt[0] < cnt[1]:
    print("bigdata?")
else:
    print("bigdata? security!")