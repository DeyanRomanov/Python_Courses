start_number = int(input())
end_number = int(input())
magic_number = int(input())

counter_first_magic = 0
total_counter = 0
flag = False

for a in range(start_number, end_number + 1):
    for b in range(start_number, end_number + 1):
        total_counter += 1
        if a + b == magic_number:
            print(f"Combination N:{total_counter} ({a} + {b} = {magic_number})")
            flag = True
            break
        if flag is True:
            break
    if flag is True:
        break
if flag is False:
    print(f"{total_counter} combinations - neither equals {magic_number}")
