s = 'aaaa'
length = 1

checker = list(map(''.join, zip(*[iter(s)] * length)))

print(checker)