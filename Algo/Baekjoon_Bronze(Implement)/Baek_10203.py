import sys

n = int(sys.stdin.readline())

vowels = "a e i o u".split(" ")

for _ in range(n):
    word = sys.stdin.readline().strip()
    counter = 0

    for check in vowels:
        counter += word.count(check)

    print("The number of vowels in {0} is {1}.".format(word, counter))