import sys

num = list(map(int, sys.stdin.readline().split()))

# 1. 주어진 네 자리 숫자로부터 시계수를 구하는 함수
def get_clock_number(nums):
    # 네 자리 숫자에서 시계 방향으로 만들어지는 4개의 숫자 중 가장 작은 값 구하기
    rotations = [
        int(''.join(map(str, nums))),  # 원래 순서
        int(''.join(map(str, nums[1:] + nums[:1]))),  # 한 칸 시계 방향 회전
        int(''.join(map(str, nums[2:] + nums[:2]))),  # 두 칸 시계 방향 회전
        int(''.join(map(str, nums[3:] + nums[:3])))  # 세 칸 시계 방향 회전
    ]
    return min(rotations)

# 2. 모든 가능한 시계수 구하기
def generate_all_clock_numbers():
    clock_numbers = set()  # 중복을 방지하기 위해 set 사용
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    nums = [a, b, c, d]
                    clock_number = get_clock_number(nums)
                    clock_numbers.add(clock_number)
    return sorted(clock_numbers)  # 오름차순으로 정렬하여 반환

# 3. 입력받은 네 자리 숫자의 시계수가 몇 번째로 작은지 구하는 함수
def find_clock_number_position(input_nums):
    # 주어진 숫자의 시계수 구하기
    clock_number = get_clock_number(input_nums)

    # 모든 가능한 시계수를 구하고, 해당 시계수가 몇 번째로 작은지 찾기
    all_clock_numbers = generate_all_clock_numbers()

    # 시계수의 인덱스를 찾아서 몇 번째인지 반환 (1부터 시작)
    return all_clock_numbers.index(clock_number) + 1

print(find_clock_number_position(num))

# 다른 사람 풀이

# import sys
# input = sys.stdin.readline
#
# def su(r):
#     sigyesu = list(map(int,str(r)))
#     rot = [0,1,2,3]*4
#     for i in range(4):
#         new_num = int(sigyesu[rot[i+1]] * 1000
#                       +sigyesu[rot[i+2]] * 100
#                       +sigyesu[rot[i+3]] * 10
#                       +sigyesu[rot[i]])
#         if new_num < r:
#             r = new_num
#     return r
#
# numbers = int(''.join(input().split()))
#
# result = su(numbers)
# ans = 0
# for i in range(1111,result+1):
#     chk = list(map(int,str(i)))
#
#     if 0 not in chk:
#         if su(i) == i:
#             ans+=1
# print(ans)