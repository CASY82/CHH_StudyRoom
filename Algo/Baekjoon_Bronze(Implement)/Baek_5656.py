i = 1

while True:
    sic = list(input().split())

    if sic[1] == 'E':
        break

    tmp = eval(''.join(sic))
    if tmp:
        result = "true"
    else:
        result = "false"

    print('Case ', i, ': ', result, sep='')

    i += 1
# i = 1
#
# while True:
#     sic = list(input().split())
#
#     if sic[1] == "E":
#         break
#
#     if sic[1] == ">":
#         result =
#
#     print(sic)