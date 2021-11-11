import pyfiglet


def ascii_art(msg):
    text = pyfiglet.figlet_format(msg)
    print(text)


message = input()

ascii_art(message)