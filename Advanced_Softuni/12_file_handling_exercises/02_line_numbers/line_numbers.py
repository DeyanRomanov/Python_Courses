with open('text.txt', 'r') as file, open('output.txt', 'w') as output:

    for index, line in enumerate(file):
        letters_count = 0
        punctuation_marks_count = 0

        for symbol in line.strip():
            if not symbol.isalpha() and not symbol == ' ':
                punctuation_marks_count += 1
            elif symbol.isalpha():
                letters_count += 1

        output.write(f"Line {index + 1}: {line.strip()} ({letters_count})({punctuation_marks_count})\n")
