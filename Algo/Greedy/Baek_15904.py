word = input()

check = ["U", "C", "P", "C"]
k = 0

for i in word:
    if k > 3:
        break
    if check[k] == i:
        k += 1

if k == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")