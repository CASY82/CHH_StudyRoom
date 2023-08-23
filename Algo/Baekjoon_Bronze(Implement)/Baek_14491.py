import sys

t = int(sys.stdin.readline())

def decimal_to_nine(decimal_num):
    if decimal_num == 0:
        return "0"

    nine_digits = ""
    while decimal_num > 0:
        remainder = decimal_num % 9
        nine_digits = str(remainder) + nine_digits
        decimal_num //= 9

    return nine_digits

nine_number = decimal_to_nine(t)
print(nine_number)