import re


number_of_barcodes = int(input())

pattern = r"^@{1}#+([A-Z]+[A-Za-z0-9]{4,}[A-Z]+)@{1}#+$"
for barcodes in range(number_of_barcodes):
    barcode = input()
    result = re.finditer(pattern, barcode)
    is_code = False
    for res in result:
        is_code = True
        product_group = ''
        for letter in res.group():
            if letter.isnumeric():
                product_group += letter
        if len(product_group) > 0:
            print(f'Product group: {product_group}')
        else:
            print('Product group: 00')
    if not is_code:
        print("Invalid barcode")
