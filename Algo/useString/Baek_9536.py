import sys

t = int(sys.stdin.readline())

for _ in range(t):
    sound = sys.stdin.readline().strip().split()
    compare = ['what', 'does', 'the', 'fox', 'say?']

    while True:
        checking = sys.stdin.readline().split()

        if compare == checking:
            break

        for i in range(len(checking)):
            if checking[i] == 'goes':
                tmp = checking[i+1:]
                break

        for j in range(len(sound)):
            for k in tmp:
                if sound[j] == k:
                    sound[j] = ''

    sound = ' '.join(sound).split()
    print(' '.join(sound))