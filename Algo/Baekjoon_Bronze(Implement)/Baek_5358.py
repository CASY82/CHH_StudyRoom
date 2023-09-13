import sys

while True:
    s_name = sys.stdin.readline().strip()

    if s_name == "":
        break

    result = ""

    for word in s_name:
        if word == "i":
            result += "e"
        elif word == "I":
            result += "E"
        elif word == "e":
            result += "i"
        elif word == "E":
            result += "I"
        else:
            result += word

    print(result)