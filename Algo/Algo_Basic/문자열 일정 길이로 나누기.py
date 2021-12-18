s = 'aaaa'
length = 1

checker = list(map(''.join, zip(*[iter(s)] * length)))

print(checker)




seq='f09f9989x'; length=2; [seq[i:i+length] for i in range(0, len(seq), length)]

# 결과
# ['f0', '9f', '99', '89', 'x']
seq='f09f9989x'; length=2; [''.join(x) for x in zip(*[list(seq[z::length]) for z in range(length)])]

# 결과
#['f0', '9f', '99', '89']
seq='f09f9989x'; length=2; map(''.join, zip(*[iter(seq)]*length))

# 결과
# ['f0', '9f', '99', '89']