import sys

n = int(sys.stdin.readline())
ingredients = list(sys.stdin.readline().strip().split())
cheese_check = set()

for i in range(n):
    if ingredients[i][-6:] == "Cheese":
        cheese_check.add(ingredients[i])

if len(cheese_check) >= 4:
    print("yummy")
else:
    print("sad")