num = ""
result = 0

while True:
    try:
        inputer = input()
        if inputer == "":
            break
        num += inputer
    except:
        break

for i in num.split(","):
    result += int(i)

print(result)