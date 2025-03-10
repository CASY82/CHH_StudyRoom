import sys

a, b, c = map(int, sys.stdin.readline().split())

normal_cuisine = dict()
special_cuisine = dict()
service_cuisine = set()

for _ in range(a):
    n_food, n_cost = sys.stdin.readline().strip().split()
    normal_cuisine[n_food] = int(n_cost)

for _ in range(b):
    s_food, s_cost = sys.stdin.readline().strip().split()
    special_cuisine[s_food] = int(s_cost)

for _ in range(c):
    sv_food = sys.stdin.readline().strip()
    service_cuisine.add(sv_food)

n = int(sys.stdin.readline())
customer_service_pick = []
customer_normal_pick = []
customer_special_pick = []
customer_n_cost = 0
customer_s_cost = 0
total = 0
res = True

for _ in range(n):
    food = sys.stdin.readline().strip()

    if food in normal_cuisine:
        customer_n_cost += normal_cuisine[food]
        customer_normal_pick.append(food)
    elif food in special_cuisine:
        customer_s_cost += special_cuisine[food]
        customer_special_pick.append(food)
    else:
        customer_service_pick.append(food)

if len(customer_special_pick) >= 1 and customer_n_cost < 20000:
    res = False

if len(customer_service_pick) == 1 and customer_n_cost + customer_s_cost < 50000:
    res = False

if len(customer_service_pick) > 1:
    res = False

if res:
    print("Okay")
else:
    print("No")