budget = float(input())
flour = float(input())


eggs_pack = flour * 0.75
milk_price = (flour * 1.25) / 4
cozonacs_price = flour + eggs_pack + milk_price
cozonacs_counter = 0
total_cozonacs = 0
colored_eggs = 0


while budget > 0:
    if budget < cozonacs_price:
        break
    else:
        budget -= cozonacs_price
        cozonacs_counter += 1
        total_cozonacs += 1
        colored_eggs += 3
    if cozonacs_counter == 3:
        colored_eggs -= total_cozonacs - 2
        cozonacs_counter = 0

print(f"You made {total_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
