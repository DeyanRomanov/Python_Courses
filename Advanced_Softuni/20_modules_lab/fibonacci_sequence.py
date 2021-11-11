from test_modules.mathematical_operations import fibonacci_sequence_func, locate_func

commands = input()

fibonacci = []

while not commands == 'Stop':
    commands = commands.split()
    command, number = commands[0], int(commands[-1])
    if command == 'Create':
        fibonacci = fibonacci_sequence_func(number)
        print(f"{' '.join(str(x) for x in fibonacci)}")
    elif command == 'Locate':
        print(locate_func(fibonacci, number))
    commands = input()
