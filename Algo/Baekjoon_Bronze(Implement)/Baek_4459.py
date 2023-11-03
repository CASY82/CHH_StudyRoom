import sys

n = int(sys.stdin.readline())

rules = dict()

for i in range(n):
    rules[i + 1] = sys.stdin.readline().strip()

t = int(sys.stdin.readline())

for _ in range(t):
    rule = int(sys.stdin.readline())

    if rule not in rules:
        print("Rule {}: No such rule".format(rule))
    else:
        print("Rule {0}: {1}".format(rule, rules[rule]))