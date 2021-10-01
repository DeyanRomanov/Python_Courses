def characters_range(first_symbol, second_symbol):
    symbol_list = []
    for symbol in range(ord(first_symbol) + 1, ord(second_symbol)):
        symbol_list.append(chr(symbol))
    symbol_list = ' '.join(symbol_list)
    return symbol_list


start_symbol = input()
finish_symbol = input()

print(characters_range(start_symbol, finish_symbol))
