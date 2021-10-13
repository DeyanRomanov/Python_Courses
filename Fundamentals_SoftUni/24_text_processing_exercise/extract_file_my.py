path = input()
path = path[::-1]
# File name: Template
# File extension: pptx
file_name = ''
extension = ''

for letter in path:
    if not letter == '.':
        extension += letter
    else:
        break

path = path.replace('.', '')
path = path.replace(extension, '')

for letter in path:
    if not letter == chr(92):
        file_name += letter
    else:
        break

print(f'File name: {file_name[::-1]}')
print(f'File extension: {extension[::-1]}')
