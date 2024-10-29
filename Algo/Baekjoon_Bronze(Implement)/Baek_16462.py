import sys

def replace_numbers(input_string):
    return input_string.replace('6', '9').replace('0', '9')

def custom_round(number):
    if number % 1 >= 0.5:
        return int(number) + 1
    else:
        return int(number)

n = int(sys.stdin.readline())

total = 0

for _ in range(n):
    score = sys.stdin.readline().strip()

    if score != "100":
        total += int(replace_numbers(score))
    else:
        total += 100

print(custom_round(total / n))