from os import remove

ERROR_MESSAGE = "An error occurred"


def create_new_file(file_name):
    with open(file_name, "w") as file:
        file.write("")


def add_content_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(f"{content}\n")


def replace_file_content(file_name, old_string, new_string):
    try:
        with open(file_name, "r+") as file:
            current_content = file.read()
            edited_content = current_content.replace(old_string, new_string)
            file.seek(0)
            file.write(edited_content)
    except FileNotFoundError:
        print(ERROR_MESSAGE)


def delete_file(file_name):
    try:
        remove(file_name)
    except FileNotFoundError:
        print(ERROR_MESSAGE)


commands_mapper = {
    "Create": create_new_file,
    "Add": add_content_to_file,
    "Replace": replace_file_content,
    "Delete": delete_file,
}

line = input()

while not line == "End":
    command_data = line.split("-")

    command, command_args = command_data[0], command_data[1:]

    commands_mapper[command](*command_args)

    line = input()
