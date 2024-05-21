import sys

sentence = sys.stdin.readline().strip()

if sentence[-5:] == "driip":
    print("cute")
else:
    print("not cute")