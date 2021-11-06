CHARS_FOR_REPLACING = ("-", ",", ".", "!", "?")


def get_file_content(file_name, mode):
    with open(file_name, mode) as file:
        return file.readlines()


def get_text_even_lines(text):
    even_lines = []
    for index in range(len(text)):
        if index % 2 == 0:
            even_lines.append(text[index])
    return even_lines


def replace_chars(text):
    for index in range(len(text)):
        for char in CHARS_FOR_REPLACING:
            if char in text[index]:
                text[index] = text[index].replace(char, "@")
    return text


def reverse_words_order(text):
    for index in range(len(text)):
        reversed_line = " ".join(reversed(text[index].split()))
        text[index] = reversed_line
    return text


content_file_name = "text.txt"
read_mode = "r"

text_lines = get_file_content(content_file_name, read_mode)

text_lines = get_text_even_lines(text_lines)

text_lines = replace_chars(text_lines)

text_lines = reverse_words_order(text_lines)

[print(line) for line in text_lines]
