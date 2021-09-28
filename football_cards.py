team_a = []
team_b = []

for a in range(1, 12):
    a = f'A-{a}'
    team_a.append(a)

for b in range(1, 12):
    b = f'B-{b}'
    team_b.append(b)

cards = input()

cards = cards.split(' ')

is_terminated = False
counter_a = 0
counter_b = 0

for card in cards:
    if card in team_a:
        counter_a += 1
        team_a.remove(card)
    elif card in team_b:
        counter_b += 1
        team_b.remove(card)
    if counter_a == 5 or counter_b == 5:
        is_terminated = True
        break

print(f"Team A - {11 - counter_a}; Team B - {11 - counter_b}")
if is_terminated:
    print("Game was terminated")

# team_a = [f'A-{num}' for num in range(1, 12)]
# team_b = [f'B-{num}' for num in range(1, 12)]
#
# players_with_red_card = list(set(input().split()))
# is_terminated = False
#
# while len(players_with_red_card) > 0:
#     for player in players_with_red_card:
#         if player in team_a:
#             team_a.remove(player)
#             players_with_red_card.remove(player)
#         if player in team_b:
#             team_b.remove(player)
#             players_with_red_card.remove(player)
#         if len(team_a) < 7 or len(team_b) < 7:
#             is_terminated = True
#             break
#     if is_terminated:
#         break
#
# print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
# if is_terminated:
#     print('Game was terminated')
