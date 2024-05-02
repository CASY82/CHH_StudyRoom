import sys

lv, correct = sys.stdin.readline().strip().split()

lv = int(lv)

if correct == "miss":
    print(0)
elif correct == "bad":
    print(lv * 200)
elif correct == "cool":
    print(lv * 400)
elif correct == "great":
    print(lv * 600)
elif correct == "perfect":
    print(lv * 1000)