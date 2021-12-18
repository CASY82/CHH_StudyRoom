import sys

n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))

location = [(i+1) for i in range(n)]

for i in range(n):
    cnt = 0
    for j in range(n):
        if (i+1) < location[j]:
            cnt += 1
            if cnt == people[i] and j > location.index(i+1):
                location[location.index(i+1)], location[j] = location[j], location[location.index(i+1)]
                break

            if cnt > people[i] and location.index(i+1) > j:
                location[location.index(i + 1)], location[j] = location[j], location[location.index(i + 1)]
                break


for i in location:
    print(i, end=' ')


#반례
# 10
# 5 3 7 1 4 2 1 0 0 0
#
# 8 4 7 2 6 1 9 5 10 3

# 참고 코드1 (insert를 이용하는 방법이다. n-1-i번째 자리에 n-i를 넣으면 된다는걸 이용한 방법인거 같다. 저 식을 왜 생각 못했을까...
# import sys
#
# n = int(sys.stdin.readline())
# data = list(map(int, sys.stdin.readline().split()))
# answer = []
#
# for i in range(n):
#     answer.insert(data[n - 1 - i], n - i)
#     print(answer)
#
# for i in answer:
#     print(i, end=' ')
