import sys

score = "A+,A0,B+,B0,C+,C0,D+,D0,F,P".split(",")
score_num = "4.5 4.0 3.5 3.0 2.5 2.0 1.5 1.0 0.0".split(" ")

hak_sum = 0
tmp = 0

for _ in range(20):
    name, hak, score_you = sys.stdin.readline().split()
    hak = float(hak)

    if score_you == "P":
        continue

    hak_sum += hak
    tmp += hak * float(score_num[score.index(score_you)])

print("%.6f" % (tmp / hak_sum))