person = int(input())
location = list(map(int, input().split()))

pc = [False] * 101
count = 0

for i in range(person):
    if pc[location[i]] == False:
        pc[location[i]] = True
    else:
        count += 1

print(count)