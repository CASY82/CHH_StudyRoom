x_price = int(input())
y_gen_price = int(input())
y_gen_line = int(input())
y_add_price = int(input())
use_water = int(input())

x = x_price * use_water
if use_water > y_gen_line:
    y = y_gen_price + (use_water - y_gen_line) * y_add_price
else:
    y = y_gen_price

print(min(x, y))