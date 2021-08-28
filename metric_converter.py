length = float(input())
metric = str(input())
new_metric = str(input())
area = 0
if metric == 'mm':
    if new_metric == 'cm':
        area = length / 10
    elif new_metric == 'm':
        area = length / 1000
elif metric == 'cm':
    if new_metric == 'mm':
        area = length * 10
    elif new_metric == 'm':
        area = length / 100
elif metric == 'm':
    if new_metric == 'mm':
        area = length * 1000
    elif new_metric == 'cm':
        area = length * 100
print(f'{area:.3f}')
