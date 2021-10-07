def is_valid(elements, indx_1, indx_2):
    if 0 > indx_1 or indx_1 >= len(elements) or 0 > indx_2 or indx_2 >= len(elements) or indx_1 == indx_2:
        print(f"Invalid input! Adding additional elements to the board")
        return False
    return True


def the_same_indexes(elements, count):
    a = len(elements) // 2
    count = '-' + str(count) + 'a'
    elements.insert(a, count)
    elements.insert(a, count)
    return elements


def remove_elements(elements, indx_1, indx_2):
    a = elements[indx_1]
    elements.remove(a)
    elements.remove(a)
    return elements


games_elements = input().split()
hits = input()
moving_counter = 0

while not hits == 'end':
    moving_counter += 1
    index_1, index_2 = [int(index) for index in hits.split()]
    if not is_valid(games_elements, index_1, index_2):
        games_elements = the_same_indexes(games_elements, moving_counter)
    else:
        if games_elements[index_1] == games_elements[index_2]:
            print(f"Congrats! You have found matching elements - {games_elements[index_2]}!")
            games_elements = remove_elements(games_elements, index_1, index_2)
        elif not games_elements[index_1] == games_elements[index_2]:
            print(f"Try again!")
    if len(games_elements) == 0:
        print(f"You have won in {moving_counter} turns!")
        break
    hits = input()

if len(games_elements) > 0:
    print(f"Sorry you lose :(\n{' '.join(games_elements)}")
