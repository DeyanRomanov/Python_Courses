def solution(numbers, queries):
    if not isinstance(numbers, list) and not isinstance(queries, list):
        return
    result = []
    total = 0
    for query in queries:
        if len(query) == 3:
            start = query[0]
            end = query[1]
            additional = query[2]
            selection = numbers[start-1:end]
            has_zeros = False
            for el in selection:
                if el == 0:
                    has_zeros = True
            print(f"has_zeros: {has_zeros}")
            print(f"selection: {selection}")
            total = sum(selection)
            if has_zeros:
                total += additional
            result.append(total)
    return result
