import sys

def check_symbol(string):
    symbols = "+_)(*&^%$#@!./,;{}"  # 기호 집합

    for symbol in symbols:
        if symbol in string:
            return True

    return False

t = int(sys.stdin.readline())

for _ in range(t):
    length = int(sys.stdin.readline())
    password = sys.stdin.readline().strip()
    result = True

    if length < 12:
        result = False
    else:
        if not any(c.isupper() for c in password):
            result = False

        if not any(c.islower() for c in password):
            result = False

        if not any(c.isdigit() for c in password):
            result = False

        if not check_symbol(password):
            result = False

    if result:
        print("valid")
    else:
        print("invalid")