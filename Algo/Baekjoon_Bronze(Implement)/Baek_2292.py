n = int(input())

tier = 1
num = 1

while n > num:
    num += 6 * tier
    tier += 1

print(tier)