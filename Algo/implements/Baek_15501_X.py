#어떤 방식이든 첫번째 순열 순서를 기준으로 다시 나열해서 배열 순서만 맞게 하면 됨...
import sys

n = int(sys.stdin.readline())

first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

# 정방향 순서 밀기
idx = second.index(first[0])
new_arr = second[idx:] + second[:idx]

# 역방향
second.reverse()
rev_idx = second.index(first[0])
rev_new_arr = second[rev_idx:] + second[:rev_idx]

if first == rev_new_arr or first == new_arr:
    print("good puzzle")
else:
    print("bad puzzle")