def combination(names, index, chairs, combinations):
    if len(combinations) == chairs:
        print(', '.join(combinations))
        return
    for i in range(index, len(names)):
        combinations.append(names[i])
        combination(names, i + 1, chairs, combinations)
        combinations.pop()


names_of_child = input().split(', ')
number_of_chairs = int(input())
total_combinations = []

combination(names_of_child, 0, number_of_chairs, total_combinations)
