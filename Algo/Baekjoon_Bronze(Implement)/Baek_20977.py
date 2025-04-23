import sys

n = int(sys.stdin.readline())
word = list(sys.stdin.readline().strip())

j_stock = 0
o_stock = 0
i_stock = 0

for i in range(n):
    if word[i] == "J":
        j_stock += 1
    elif word[i] == "O":
        o_stock += 1
    else:
        i_stock += 1

res = "J" * j_stock + "O" * o_stock + "I" * i_stock
print(res)