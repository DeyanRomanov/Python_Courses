man_clients = int(input())
woman_clients = int(input())
tables_in_restourant = int(input())
table_counter = 0
for man in range(1, man_clients + 1):
    for woman in range(1, woman_clients + 1):
        table_counter += 1
        if table_counter <= tables_in_restourant:
            print(f'({man} <-> {woman})', end=' ')
