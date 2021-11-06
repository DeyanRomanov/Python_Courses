import os

result = {}

first_split = input()   # you must press '.' to run , and just check your desktop :)
for root, _, files in os.walk(os.getcwd()):
    for file in files:
        ext = file.split(f'{first_split}')[-1]
        if ext not in result:
            result[ext] = []
        result[ext].append(os.path.join(root, file))


with open(os.path.expanduser("~/Desktop/report.txt"), 'w') as result_files:
    for ext, files in sorted(result.items()):
        result_files.write(f'.{ext}\n')
        for file in sorted(files):
            file = "".join(file.split("\\")[-1])
            result_files.write(f'--- {file}')
            result_files.write('\n')
