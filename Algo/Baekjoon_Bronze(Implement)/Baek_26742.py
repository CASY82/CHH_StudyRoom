import sys

socks = sys.stdin.readline().strip()

white = socks.count("B")
black = socks.count("C")

print(white // 2 + black // 2)