start_symbol = int(input())
finish_symbol = int(input())

for symbol in range(start_symbol, finish_symbol + 1):
    print(chr(symbol), end=' ')
