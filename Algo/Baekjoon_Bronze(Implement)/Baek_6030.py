import sys

p, q = map(int, sys.stdin.readline().split())

def find_divisors(number):
  divisors = []
  for i in range(1, number + 1):
    if number % i == 0:
      divisors.append(i)
  return divisors

tmp_p = find_divisors(p)
tmp_q = find_divisors(q)

for i in range(len(tmp_p)):
    for j in range(len(tmp_q)):
        print(tmp_p[i], tmp_q[j])