import itertools


def possible_permutations(nums):
    for perm in list(itertools.permutations(nums)):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]