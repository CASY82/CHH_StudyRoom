import sys

while True:
    sentense = list(sys.stdin.readline().strip().split())
    result = True

    if sentense[0] == '*':
        break

    diff = sentense[0][0].upper()

    for word in sentense:
        word = word.upper()
        if diff != word[0]:
            result = False

    if result:
        print("Y")
    else:
        print("N")