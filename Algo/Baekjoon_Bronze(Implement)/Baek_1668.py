# 반례를 생각 못해서 하나 틀림... 앞으로는 좀 더 깊게 생각하자

n = int(input())
trophy = []

for i in range(n):
    trophy.append(int(input()))

def counting(trophy):
    count = 0
    top = 0

    for j in trophy:
        if top < j:
            top = j
        else:
            continue

        if max(trophy) >= top:
            count += 1
            if max(trophy) == top:
                break

    return count


print(counting(trophy))
print(counting(list(reversed(trophy))))

# 숏코딩 예제
# s=[int(input())for _ in[0]*int(input())]
# def g(l):
#     m,c=0,0
#     for i in l:
#         if m<i:m,c=i,c+1
#     print(c)
# g(s)
# g(s[::-1])

# 좀 더 간단하게 되었을거 같은... 내 로직이 좀더 복잡해 보이긴 한다.
# n = int(input())
# heights = []
# for _ in range(n):
#     h = int(input())
#     heights.append(h)
#
#
# def count(array):
#     now = array[0]
#     result = 1
#     for i in range(1, len(array)):
#         if array[i] > now:
#             result += 1
#             now = array[i]
#     return result
#
#
# print(count(heights))
# heights.reverse()
# print(count(heights))