import sys

sentense = sys.stdin.readline().strip()

happy = sentense.count(":-)")
unhappy = sentense.count(":-(")

if happy >0 or unhappy > 0:
    if happy > unhappy:
        print("happy")
    elif happy < unhappy:
        print("sad")
    else:
        print("unsure")
else:
    print("none")