import sys

n = int(sys.stdin.readline())
word = "WelcomeToSMUPC"

print(word[n % len(word) - 1])