# Go Latin
import sys

n = int(sys.stdin.readline())

suffix = {
    "a": "as",
    "i": "ios",
    "y": "ios",
    "l": "les",
    "n": "anes",
    "ne": "anes",
    "o": "os",
    "r": "res",
    "t": "tas",
    "u": "us",
    "v": "ves",
    "w": "was"
}

for _ in range(n):
    word = sys.stdin.readline().strip()

    if word.endswith("ne"):
        base = word[:-2]
        print(base + suffix["ne"])
    else:
        last = word[-1]
        if last in suffix:
            base = word[:-1]
            print(base + suffix[last])
        else:
            print(word + "us")