import sys

def recursion(s, l, r):
    cnt[0] += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(sys.stdin.readline())
cnt = [0]

for _ in range(n):
    word = sys.stdin.readline().strip()

    print(isPalindrome(word), cnt[0])
    cnt[0] = 0