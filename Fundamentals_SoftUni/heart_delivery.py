neighborhoods = list(map(lambda x: int(x), input().split('@')))
cupid_jump = input()
index = 0

while not cupid_jump == 'Love!':
    cupid_jump = cupid_jump.split()
    index += int(cupid_jump[-1])
    if index >= len(neighborhoods):
        index = 0
    if neighborhoods[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighborhoods[index] -= 2
        if neighborhoods[index] == 0:
            print(f"Place {index} has Valentine's day.")

    cupid_jump = input()

failed_list = [int(num) for num in neighborhoods if num > 0]
print(f"Cupid's last position was {index}.")
if max(neighborhoods) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(failed_list)} places.")
