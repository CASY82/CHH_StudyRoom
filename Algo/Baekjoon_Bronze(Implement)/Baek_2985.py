import sys

a, b, c = sys.stdin.readline().strip().split()

num = ["" for _ in range(5)]

num[0] = a
num[2] = b
num[4] = c

sign = ["+", "-", "/", "*"]
loc = [1, 3]

for i in range(4):
    for j in range(2):
        num[loc[j]] = sign[i]
        num[loc[j-1]] = "="

        if loc[j-1] == 1:
            if int(eval("".join(num[2:5]))) == int(num[0]):
                print("".join(num))
        else:
            if int(eval("".join(num[0:3]))) == int(num[4]):
                print("".join(num))

#다른 사람 풀이 ㄷㄷ

# a,b,c = map(int,input().split())
# if a == b+c:
#   print(f"{a}={b}+{c}")
# elif a == b-c:
#   print(f"{a}={b}-{c}")
# elif a == b*c:
#   print(f"{a}={b}*{c}")
# elif a == b//c:
#   print(f"{a}={b}/{c}")
# elif c == a+b:
#   print(f"{a}+{b}={c}")
# elif c == a-b:
#   print(f"{a}-{b}={c}")
# elif c == a*b:
#   print(f"{a}*{b}={c}")
# elif c == a//b:
#   print(f"{a}/{b}={c}")