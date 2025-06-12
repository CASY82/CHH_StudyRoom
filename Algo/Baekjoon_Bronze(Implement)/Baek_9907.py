import sys

n = sys.stdin.readline().strip()
tmp = 0
check = [2, 7, 6, 5, 4, 3, 2]
mod_check = ["J", "A", "B", "C", "D", "E", "F", "G", "H", "I", "Z"]

for i in range(len(n)):
    tmp += int(n[i]) * check[i]

mod = tmp % 11

print(mod_check[mod])