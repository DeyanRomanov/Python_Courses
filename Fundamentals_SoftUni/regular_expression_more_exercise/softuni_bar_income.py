import re

total_income = 0
pattern = r"\w*\%(?P<customer>[A-Z]{1}[a-z]+)\%\w*\<(?P<product>[\D{1,}]+)\>\w*\|(?P<count>[0-9]+)\|\D*(?P<price>[" \
          r"0-9]*\.?[0-9]*)\$"
barcode_income = input()
while not barcode_income == 'end of shift':
    matches = re.finditer(pattern, barcode_income)
    for match in matches:
        if match.group('customer') and match.group('product') and match.group('count') and match.group('price'):
            customer = match.group('customer')
            product = match.group('product')
            count = float(match.group('count'))
            price = float(match.group('price'))
            income = f"{count * price:.2f}"
            print(f"{match.group('customer')}: {match.group('product')} - {income}")
            total_income += float(income)
    barcode_income = input()

print(f"Total income: {total_income:.2f}")
