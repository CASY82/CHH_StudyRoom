first, second, third, forth, fifth = map(int, input().split())

print(((first ** 2) + (second ** 2) + (third ** 2) + (forth ** 2) + (fifth ** 2)) % 10)