import sys

num = sys.stdin.readline().strip()

if len(num) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    a1 = int(num[0])
    diff = int(num[1]) - int(num[0])

    for i in range(len(num)):
        if a1 + i * diff != int(num[i]):
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            exit()
            break

    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")