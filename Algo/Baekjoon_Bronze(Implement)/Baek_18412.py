import sys

n, a, b = map(int, sys.stdin.readline().split())
words = sys.stdin.readline().strip()

new_words = words[:a - 1] + words[a - 1:b][::-1] + words[b:]

print(new_words)