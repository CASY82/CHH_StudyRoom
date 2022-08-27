import sys

n = int(sys.stdin.readline())
func = []
result = 0

for _ in range(n):
    func.append(list(map(int, sys.stdin.readline().split())))

func.sort(key= lambda x : (x[0], x[1]))

for num in range(1, n+1):
    result += func[num-1][0] * num + func[num-1][1]

print(result)