from string import punctuation, ascii_letters


def get_file_content(file_name, mode):
    with open(file_name, mode) as file:
        return file.readlines()


def get_chars_count(line, chars_list):
    return len([char for char in line if char in chars_list])


def get_formatted_line(line, line_n, letters_n, punctuations_n):
    return f"Line {line_n}: {line.rstrip()} ({letters_n})({punctuations_n})\n"


def add_line_to_file(line, file_name, mode):
    with open(file_name, mode) as file:
        file.write(line)


content_file_name = "text.txt"
read_mode = "r"

result_file_name = "result.txt"
append_mode = "a"

text_lines = get_file_content(content_file_name, read_mode)

for index in range(len(text_lines)):
    current_line = text_lines[index]
    line_number = index + 1

    letters_count = get_chars_count(current_line, ascii_letters)
    punctuations_count = get_chars_count(current_line, punctuation)

    formatted_line = get_formatted_line(current_line, line_number, letters_count, punctuations_count)

    add_line_to_file(formatted_line, result_file_name, append_mode)
