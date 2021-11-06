import os


def create_file(name_of_file):
    file = open(name_of_file, 'w')
    file.close()
    return name_of_file


def add_file(name_of_file, message):
    file = open(name_of_file, 'a')
    file.write(message)
    file.write('\n')
    file.close()
    return name_of_file


def replace_file(name_of_file, old_message, new_message):
    if os.path.isfile(name_of_file):
        file = open(name_of_file, 'r')
        data = file.read()
        data = data.replace(old_message, new_message)
        file.close()
        file = open(name_of_file, 'w')
        file.write(data)
        file.close()
        return name_of_file
    else:
        print("An error occurred")


commands = input()

while not commands == 'End':
    commands = commands.split('-')
    command = commands[0]
    if command == 'Create':
        file_name = commands[1]
        create_file(file_name)
    elif command == 'Add':
        file_name, text = commands[1::]
        add_file(file_name, text)
    elif command == 'Replace':
        file_name, old_text, new_text = commands[1::]
        replace_file(file_name, old_text, new_text)
    elif command == 'Delete':
        file_name = commands[1]
        if os.path.isfile(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    commands = input()
