a = str('%.300f' % (1/(2 ** int(input()))))

for i in range(len(a)-1, 0, -1):
    if a[i] == '0':
        a = a[:-1]
    else:
        break

print(a)
