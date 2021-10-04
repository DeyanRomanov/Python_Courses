old_version = [int(x) for x in input().split('.')]
index_one, index_two, index_three = old_version[0], old_version[1], old_version[2]


if index_three < 9:
    index_three += 1
else:
    index_three = 0
    if index_two < 9:
        index_two += 1
    else:
        index_two = 0
        index_one += 1

next_version = [index_one, index_two, index_three]

next_version = [str(x) for x in next_version]

print('.'.join(next_version))
