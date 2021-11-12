ham_price = []
drink_price = []

for _ in range(3):
    ham_price.append(int(input()))

for _ in range(2):
    drink_price.append(int(input()))

low = 100000

for i in range(3):
    for j in range(2):
        if ham_price[i] + drink_price[j] - 50 < low:
            low = ham_price[i] + drink_price[j] - 50

print(low)