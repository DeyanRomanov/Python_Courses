last_sector = input()
rows = int(input())
seats_in_row = int(input())

seats_in_row_a = seats_in_row
total_seats = 0

for sector in range(65, ord(last_sector) + 1):
    for row in range(1, rows + 1):
        if row % 2 == 0:
            seats_in_row_a += 2
        else:
            seats_in_row_a = seats_in_row
        for seats in range(97, 97 + seats_in_row_a):
            total_seats += 1
            print(f'{chr(sector)}{row}{chr(seats)}')
    rows += 1
print(total_seats)
