import sys

peppers = {
    "Poblano" : 1500,
    "Mirasol" : 6000,
    "Serrano" : 15500,
    "Cayenne" : 40000,
    "Thai" : 75000,
    "Habanero" : 125000
}

n = int(sys.stdin.readline())
total = 0

for _ in range(n):
    pepper = sys.stdin.readline().strip()

    total += peppers[pepper]

print(total)