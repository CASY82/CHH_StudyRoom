import sys

def my_round(num, ndigits=0):
    if ndigits >= 0:
        multiplier = 10 ** ndigits
        return int(num * multiplier + 0.5) / multiplier
    else:
        multiplier = 10 ** abs(ndigits)
        return int(num / multiplier + 0.5) * multiplier

n = int(sys.stdin.readline())

score = []

if n != 0:
    for _ in range(n):
        score.append(int(sys.stdin.readline()))

    score.sort()
    trimmed_mean = my_round(n * 0.15, 0)
    trimmed_mean = int(trimmed_mean)

    tmp = score[trimmed_mean:len(score) - trimmed_mean]

    print(int(my_round(sum(tmp) / len(tmp), 0)))
else:
    print(0)