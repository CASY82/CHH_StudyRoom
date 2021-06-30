#해시 1 완주하지 못한 선수
a = ["mislav", "stanko", "mislav", "ana"]
b = ["stanko", "ana", "mislav"]



def test(a,b):
    a.sort()
    b.sort()
    for i,j in zip(a,b):
        if i != j:
            return i
    return a.pop()

print(test(a,b))