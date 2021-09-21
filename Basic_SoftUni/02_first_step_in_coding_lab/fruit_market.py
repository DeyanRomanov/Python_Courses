price_strawbery = float(input())
bananas_kg = float(input())
orange_kg = float(input())
malini_kg = float(input())
strawbery_kg = float(input())
price_malini = price_strawbery / 2
price_orange = price_malini * 0.6
price_bananas = price_malini * 0.2
need_funds = price_bananas * bananas_kg + price_strawbery * strawbery_kg +\
             orange_kg * price_orange + malini_kg * price_malini
print(need_funds)
