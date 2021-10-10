countries = input().split(', ')
capitals = input().split(', ')

countries_dict = dict(zip(countries, capitals))

for key, value in countries_dict.items():
    print(f'{key} -> {value}')
