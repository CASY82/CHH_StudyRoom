import sys

#일단 1이 있는지 검사 있다면 앞의 수부터 제거
#그다음 없다면 걍 원래 수에서 1빼기

num = sys.stdin.readline().strip()
result = 0

while int(num) > 0:
    if "1" in num:
        num = num.replace("1", "", 1)
        result += 1
    else:
        num = str(int(num) - 1)
        result += 1

    if num == "":
        num = 0

print(result)