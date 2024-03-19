import sys

sentence = sys.stdin.readline().strip()

if sentence[0] == "\"" and sentence[-1] == "\"" and sentence.count("\"") == 2:
    if sentence[1:-1] == "":
        print("CE")
    else:
        print(sentence[1:-1])
else:
    print("CE")