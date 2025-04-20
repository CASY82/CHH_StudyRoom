import sys

n = int(sys.stdin.readline())

# alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
# counter = [0 for _ in range(26)]

before = sys.stdin.readline().strip()
after = sys.stdin.readline().strip()
seperator = dict()

for i in range(n):
    if after[i] not in seperator:
        seperator[after[i]] = 1
    else:
        seperator[after[i]] += 1

for j in range(n):
    if before[j] not in seperator:
        continue
    else:
        seperator[before[j]] -= 1

res = 0

for k, v in seperator.items():
    if v < 0:
        continue
    else:
       res += v

print(res)