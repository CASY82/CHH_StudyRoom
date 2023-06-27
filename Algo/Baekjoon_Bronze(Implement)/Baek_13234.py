import sys

boolsik = list(sys.stdin.readline().strip().split())

changer = {'true': 'True', 'false': 'False', 'OR': 'or', 'AND': 'and'}

if eval(changer[boolsik[0]] + " " + changer[boolsik[1]] + " " + changer[boolsik[2]]):
    print('true')
else:
    print('false')