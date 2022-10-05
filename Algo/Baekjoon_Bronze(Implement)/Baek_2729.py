import sys

t = int(sys.stdin.readline())

for _ in range(t):
      first, second = sys.stdin.readline().strip().split()

      result = int(first, 2) + int(second, 2)

      print(format(result, 'b'))