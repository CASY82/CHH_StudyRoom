import sys

n, m = map(int, sys.stdin.readline().split())

children = {}
files = {}

def touch_folder(name):
    if name not in children:
        children[name] = []
    if name not in files:
        files[name] = set()

touch_folder("main")

for _ in range(n + m):
    p, f, c = sys.stdin.readline().strip().split()
    c = int(c)

    touch_folder(p)
    if c == 1: # 폴더
        touch_folder(f)
        children[p].append(f)
    else: # 파일
        files[p].add(f)

distinct_cnt = {}
total_cnt = {}

sys.setrecursionlimit(10000)

def dfs(u):
    s = set(files[u])
    total = len(files[u])

    for v in children.get(u, []):
        cs, ct = dfs(v)
        total += ct

        if len(s) < len(cs):
            s, cs = cs, s

        s |= cs

    distinct_cnt[u] = len(s)
    total_cnt[u] = total
    return s, total

dfs("main")

q = int(sys.stdin.readline())
for _ in range(q):
    path = sys.stdin.readline().strip()
    folder = path.split('/')[-1]
    print(distinct_cnt[folder], total_cnt[folder])