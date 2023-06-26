import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

adj = []
noun = []

for _ in range(n):
    adj.append(sys.stdin.readline().strip())

for _ in range(m):
    noun.append(sys.stdin.readline().strip())

for i in range(n):
    for j in range(m):
        print("{0} as {1}".format(adj[i], noun[j]))