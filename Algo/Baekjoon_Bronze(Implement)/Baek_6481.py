import sys

emoji_set = {
    "CU" : "see you",
    ":-)" : "I’m happy",
    ":-(" : "I’m unhappy",
    ";-)" : "wink",
    ":-P" : "stick out my tongue",
    "(~.~)" : "sleepy",
    "TA" : "totally awesome",
    "CCC" : "Canadian Computing Competition",
    "CUZ" : "because",
    "TY" : "thank-you",
    "YW" : "you’re welcome"
}

while True:
    emoji = sys.stdin.readline().strip()

    if emoji == "TTYL":
        print("talk to you later")
        break

    if emoji not in emoji_set:
        print(emoji)
    else:
        print(emoji_set[emoji])