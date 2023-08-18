import sys
import math

width, height = map(int, sys.stdin.readline().split())

field_yard = width * height
acre = 4840
corn_seed = 5 * acre

print(int(math.ceil(field_yard / corn_seed)))