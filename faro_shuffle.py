cards = input().split(' ')
shuffles = int(input())

last_shuffled = []
# first_half = cards[0:int((len(cards)/2))]
# second_half = cards[int((len(cards)/2))::]

for card in range(1, shuffles + 1):
    first_half = cards[0:int((len(cards) / 2))]
    second_half = cards[int((len(cards) / 2)):]
    for shuffle in range(int(len(cards)/2)):
        last_shuffled.append(first_half[shuffle])
        last_shuffled.append(second_half[shuffle])
    cards = last_shuffled
    last_shuffled = []
print(cards)
