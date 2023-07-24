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

# 다른 사람 풀이 참고

# aw={"Paper":57.99,"Printer":120.50,"Planners":31.25,"Binders":22.50,"Calendar":10.95,"Notebooks"	:11.20,"Ink":66.95}
# su=0
# while 1:
#     try:
#         su+=aw[input()]
#     except:
#         break
# print(f"${su}")