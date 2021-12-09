#어찌 혼자 풀었는데 다른사람들이 푼 풀이랑 비슷하다... 신기하네...
import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

tmp = list(set(num))
tmp.sort()
num_dic = dict()
for i, v in enumerate(tmp):
    num_dic[v] = i

for i in num:
    print(num_dic[i], end=' ')