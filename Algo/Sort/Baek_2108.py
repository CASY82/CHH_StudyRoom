#통과는 하였으나 뭔가 억지로 푼 느낌... 좀더 효율적인 코드 작성법을 확인할 필요가 있다.
import sys
n = int(sys.stdin.readline())
num = []
bindo_val = [0] * 8001

for _ in range(n):
    a = int(sys.stdin.readline())
    num.append(a)
    bindo_val[a + 4000] += 1

num.sort()
max_cnt = 0

max_bindo = max(bindo_val)
bindo = [i for i,v in enumerate(bindo_val) if v == max_bindo]

print(round(sum(num)/len(num)))
print(num[len(num)//2])
if len(bindo) == 1:
    print(bindo[0] - 4000)
else:
    print(bindo[1] - 4000)
print(num[len(num)-1] - num[0])


#counter를 활용한 풀이.. 그리고 마지막 문제 len(num)-1 이런식으로 할 필요없이 -1쓰면된다는 사실을 잊고있었다...

# from collections import Counter
# from sys import stdin
#
# input = stdin.readline
#
# if __name__ == '__main__':
#     nums_cnt = int(input())
#     nums = []
#     for _ in range(nums_cnt):
#         num = int(input())
#         nums.append(num)
#     nums.sort()
#
#     arith_aver = round(sum(nums) / nums_cnt)
#     median = nums[nums_cnt // 2]
#     modes = Counter(nums).most_common()
#     if len(modes) > 1 and modes[0][1] == modes[1][1]:
#         mode = modes[1][0]
#     else:
#         mode = modes[0][0]
#     range_val = nums[-1] - nums[0]
#
#     print(arith_aver)
#     print(median)
#     print(mode)
#     print(range_val)

