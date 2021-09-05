# 새벽에 무리하지 말자. 머리가 안돈다.

# remain = []
# result = []
#
# now = input().split(':')
# start = input().split(':')
#
# start = list(map(int, start))
# now = list(map(int, now))
#
# if start[0] > now[0]:
#     if start[1] > now[1]:
#         remain.append(start[0] - now[0])
#         if start[2] > now[2]:
#             remain.append(start[1] - now[1])
#             remain.append(start[2] - now[2])
#         else:
#             remain.append(start[1] - now[1] - 1)
#             remain.append(60 + start[2] - now[2])
#     else:
#         remain.append(start[0] - 1 - now[0])
#         if start[2] > now[2]:
#             remain.append(60 + start[1] - now[1])
#             remain.append(start[2] - now[2])
#         else:
#             remain.append(60 + start[1] - now[1] - 1)
#             remain.append(60 + start[2] - now[2])
# else:
#     if start[1] > now[1]:
#         remain.append(24 + start[0] - now[0])
#         if start[2] > now[2]:
#             remain.append(start[1] - now[1])
#             remain.append(start[2] - now[2])
#         else:
#             remain.append(start[1] - now[1] - 1)
#             remain.append(60 + start[2] - now[2])
#     else:
#         remain.append(24 + start[0] - 1 - now[0])
#         if start[2] > now[2]:
#             remain.append(60 + start[1] - now[1])
#             remain.append(start[2] - now[2])
#         else:
#             remain.append(60 + start[1] - now[1] - 1)
#             remain.append(60 + start[2] - now[2])
#
# for i in range(3):
#         result.append(str(format((remain[i]), '02')))
#
# print(':'.join(result))


# 다른사람 풀이 참고

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t = h2*3600+m2*60+s2 - (h1*3600+m1*60+s1)
if t < 0:
    t += 60*60*24
h = t//3600
m = (t%3600)//60
s = t%60
print("%02d:%02d:%02d" % (h,m,s))