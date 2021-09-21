import sys

n = int(input())
sum_even = 0
sum_odd = 0
max_number_even = -sys.maxsize
min_number_even = sys.maxsize
max_number_odd = -sys.maxsize
min_number_odd = sys.maxsize
for x in range(1, n + 1):
    i = float(input())
    if x % 2 == 0:
        sum_even += i
        if max_number_even < i:
            max_number_even = i
        if min_number_even > i:
            min_number_even = i
    else:
        sum_odd += i
        if max_number_odd < i:
            max_number_odd = i
        if min_number_odd > i:
            min_number_odd = i
print(f'OddSum={sum_odd:.2f},')
if min_number_odd == sys.maxsize:
    print(f'OddMin=No,')
else:
    print(f'OddMin={min_number_odd:.2f},')
if max_number_odd == -sys.maxsize:
    print(f'OddMax=No,')
else:
    print(f'OddMax={max_number_odd:.2f},')
print(f'EvenSum={sum_even:.2f},')
if min_number_even == sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={min_number_even:.2f},')
if max_number_even == -sys.maxsize:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={max_number_even:.2f}')
