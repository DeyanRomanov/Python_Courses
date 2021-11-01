def fill_the_box(a, b, c, *args):
    all_cubes_capacity = []
    for number in args:
        if number == "Finish":
            break
        all_cubes_capacity.append(number)
    all_cubes_capacity = sum(all_cubes_capacity)

    box_capacity = a * b * c
    result = abs(all_cubes_capacity - box_capacity)

    if box_capacity < all_cubes_capacity:
        return f"No more free space! You have {result} more cubes."
    else:
        return f"There is free space in the box. You could put {result} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
