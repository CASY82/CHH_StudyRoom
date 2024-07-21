def to_base_12(num):
    if num == 0:
        return '0'
    digits = []
    while num:
        remainder = num % 12
        if remainder >= 10:
            # 10 이상일 경우 A, B로 변환
            if remainder == 10:
                digits.append('a')
            elif remainder == 11:
                digits.append('b')
        else:
            digits.append(str(remainder))
        num //= 12
    return ''.join(digits[::-1])


def checkAns(number):
    base_12 = to_base_12(number)
    base_16 = hex(number)[2:]

    ans_ori = 0
    ans_12 = 0
    ans_16 = 0

    for i in range(4):
        ans_ori += int(str(number)[i])

    for j in range(len(base_12)):
        if base_12[j] == "a":
            ans_12 += 10
        elif base_12[j] == "b":
            ans_12 += 11
        else:
            ans_12 += int(base_12[j])

    for k in range(len(base_16)):
        if base_16[k] == "a":
            ans_16 += 10
        elif base_16[k] == "b":
            ans_16 += 11
        elif base_16[k] == "c":
            ans_16 += 12
        elif base_16[k] == "d":
            ans_16 += 13
        elif base_16[k] == "e":
            ans_16 += 14
        elif base_16[k] == "f":
            ans_16 += 15
        else:
            ans_16 += int(base_16[k])

    if ans_ori == ans_12 == ans_16:
        return True
    else:
        return False

for i in range(1000, 10000):
    if checkAns(i):
        print(i)