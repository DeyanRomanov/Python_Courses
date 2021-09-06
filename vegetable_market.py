vegetables_kg_price = float(input())
fruits_kg_price = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())
euro = 1.94
prices = (vegetables_kg_price * vegetables_kg + fruits_kg * fruits_kg_price) / euro
print(f'{prices:.2f}')
