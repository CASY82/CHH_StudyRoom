# 이거 왜틀렸냐? 전혀 모르겠음
# from collections import deque
#
# num = deque()
#
# while True:
#     try:
#         num_tmp = input()
#         # 여기 부분이 문제인건가
#         if num_tmp == "":
#             break
#
#         tmp_array = num_tmp.split(" ")
#         for i in tmp_array:
#             num.append(int(i[::-1]))
#     except EOFError:
#         break
#
# num.popleft()
# num = list(num)
# num.sort()
# for i in num:
#     print(i)

li = list()
cnt = 0
while 1:
    try:
        ins = input()
        # 이 부분이 무슨 차이를 가져다 주는거지?
        if ins == -1:
            break
        else:
            i_sp = ins.split()
            for i in i_sp:
                if cnt != 0:
                    i = "".join(reversed(i)).lstrip("0")
                    li.append(int(i))
                cnt += 1
    except EOFError:
        break

res = sorted(li)
for i in res:
    print(i)

# 다른 사람 풀이
# first_line = input().split()
# n = int(first_line[0])
# total_list = first_line[1:]
#
# while len(total_list)<n:
#     total_list.extend(input().split())
#     # print(total_list)
#
# for i in range(len(total_list)):
#     total_list[i] = total_list[i][::-1]
#
# total_list = sorted(list(map(int, total_list)))
#
# for ele in total_list:
#     print(ele)