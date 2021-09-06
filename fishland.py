mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussels_kg = int(input())
bonito_price = mackerel_price + mackerel_price * 0.6
scad_price = sprat_price + sprat_price * 0.8
mussels_price = 7.50
total = bonito_price * bonito_kg + scad_price * scad_kg + mussels_price * mussels_kg
print(f'{total:.2f}')
