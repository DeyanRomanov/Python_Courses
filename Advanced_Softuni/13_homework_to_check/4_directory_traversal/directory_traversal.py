import os

CURRENT_FILE_NAME = "directory_traversal.py"
RESULT_FILE_NAME = "report.txt"


def extract_files(dir_path, result):
    for x in os.listdir(dir_path):
        file_with_path = os.path.join(dir_path, x)
        if os.path.isfile(file_with_path) and not x == CURRENT_FILE_NAME:
            result.append(x)
        elif os.path.isdir(file_with_path):
            result = extract_files(file_with_path, result)
    return result


def group_files_by_extension(files, result):
    for file in files:
        name, ext = file.split(".")
        if ext not in result:
            result[ext] = []
        result[ext].append(file)
    return result


def write_result_to_file(files):
    path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', RESULT_FILE_NAME)
    with open(path, "a") as file:
        for ext, names in sorted(files.items()):
            file.write(f".{ext}\n")
            for name in sorted(names):
                file.write(f"- - - {name}\n")


all_files = extract_files(os.getcwd(), [])

all_files = group_files_by_extension(all_files, {})

write_result_to_file(all_files)
