import sys

equipment_list = {
    "Paper" : 5799,
    "Printer" : 12050,
    "Planners" : 3125,
    "Binders" : 2250,
    "Calendar" : 1095,
    "Notebooks" : 1120,
    "Ink" : 6695
}

result = 0

while True:
    equipment = sys.stdin.readline().strip()

    if equipment == "EOI":
        break

    result += equipment_list[equipment]

if result != 0:
    print("$" + str(result)[:-2] + "." + str(result)[-2] + str(result)[-1])
else:
    print("$0.00")
