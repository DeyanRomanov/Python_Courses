symbols_to_replace = {"-", ",", ".", "!", "?"}


with open('text.txt', 'r') as file:
    for index, line in enumerate(file):
        for symbol in line:
            if symbol in symbols_to_replace:
                line = line.replace(symbol, '@')
        line = line.split()
        if index % 2 == 0:
            print(' '.join(reversed(line)))
