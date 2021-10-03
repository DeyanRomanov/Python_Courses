def tribonacci(numbers):
    tribanacci_list = []
    trib = []

    if numbers <= 3:
        for n in range(1, numbers + 1):
            if n < 3:
                tribanacci_list.append(1)
            if n == 3:
                tribanacci_list.append(2)
        return tribanacci_list
    tribanacci_list = [1, 1, 2]
    trib = [1, 1, 2]
    for _ in range(numbers - 3):
        tribanacci_list.append(sum(trib))
        trib.append(sum(trib))
        trib.pop(0)
    return tribanacci_list


tribonacci_num = int(input())
tribonacci_sequense = [str(x) for x in tribonacci(tribonacci_num)]

print(' '.join(tribonacci_sequense))
