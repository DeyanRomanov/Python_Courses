number_of_names = int(input())

evens = set()
odds = set()

for divide in range(1, number_of_names + 1):
    name = input()
    sum_of_letter = 0

    for letter in name:
        sum_of_letter += ord(letter)
    sum_of_letter //= divide

    if sum_of_letter % 2 == 0:
        evens.add(sum_of_letter)
    else:
        odds.add(sum_of_letter)

if sum(evens) == sum(odds):
    odds_list = list(odds.union(evens))
    print(', '.join(str(nums) for nums in odds_list))
elif sum(evens) < sum(odds):
    odds_list = list(odds.difference(evens))
    print(', '.join(str(nums) for nums in odds_list))
else:
    odds_list = list(odds.symmetric_difference(evens))
    print(', '.join(str(nums) for nums in odds_list))
