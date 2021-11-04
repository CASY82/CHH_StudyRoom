p = int(input())
case = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']

for _ in range(p):
    word = list(input())
    case_count = [0 for i in range(len(case))]

    for i in range(len(word) - 2):
        tmp = ''.join(word[i:i+3])

        for j in range(len(case)):
            if tmp == case[j]:
                case_count[j] += 1
                continue

    for k in range(len(case_count)):
        print(case_count[k], end=' ')