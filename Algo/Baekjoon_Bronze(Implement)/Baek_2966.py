Adrian = ['A', 'B', 'C']
Bruno = ['B', 'A', 'B', 'C']
Goran = ['C', 'C', 'A', 'A', 'B', 'B']
a, b, g = 0, 0, 0

n = int(input())
word = input()

for i in range(n):
    if word[i] == Adrian[i % len(Adrian)]:
        a += 1

    if word[i] == Bruno[i % len(Bruno)]:
        b += 1

    if word[i] == Goran[i % len(Goran)]:
        g += 1

max_val = max(a, b, g)

print(max_val)
if a == max_val:
    print("Adrian")
if b == max_val:
    print("Bruno")
if g == max_val:
    print("Goran")
