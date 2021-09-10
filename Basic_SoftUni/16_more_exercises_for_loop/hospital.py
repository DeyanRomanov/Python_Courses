days = int(input())
doctors = 7
not_cured = 0
cured = 0
area_not_cured = 0

for x in range(1, days + 1):
    people = int(input())
    if x % 3 == 0 and not_cured > cured:
        doctors += 1
    if doctors < people:
        not_cured += people - doctors
        area_not_cured += people - doctors
        cured += doctors
    else:
        cured += people

print(f"Treated patients: {cured}.")
print(f"Untreated patients: {area_not_cured}.")
