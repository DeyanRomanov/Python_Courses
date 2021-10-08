first_employer = int(input())
second_employer = int(input())
tird_employer = int(input())
total_clients = int(input())
working_hours = 0

while total_clients > 0:
    working_hours += 1
    if working_hours % 4 == 0:
        continue
    all_workers_per_hour = first_employer + second_employer + tird_employer
    total_clients -= all_workers_per_hour

else:
    print(f"Time needed: {working_hours}h.")
