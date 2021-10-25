numbers = input().split()

nums_dict = {}

for x in numbers:
    if x not in nums_dict:
        nums_dict[x] = 0
    nums_dict[x] += 1

for key, value in nums_dict.items():
    print(f"{float(key)} - {value} times")
