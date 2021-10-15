import re

pattern = r"(^|(?<=\s))(?P<user>[A-Za-z0-9]+[-_.A-Za-z0-9]*)@(?P<host>[A-Za-z]+[-A-Za-z]*((\.[A-Za-z])+[A-Za-z]+)+)"

emails = re.finditer(pattern, input())

for email in emails:
    print(email.group())
