import sys

loc = ['P', 'K', 'H', 'T']
cards = [13, 13, 13, 13]

lost_set = set()

lost_card = sys.stdin.readline().strip()
lost_card_list = [lost_card[i:i+3] for i in range(0, len(lost_card), 3)]

for card in lost_card_list:
    if card not in lost_set:
        lost_set.add(card)
        cards[loc.index(card[0])] -= 1
    else:
        print("GRESKA")
        exit()

print(*cards)