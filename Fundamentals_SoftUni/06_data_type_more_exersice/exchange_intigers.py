# Before:
# a = 5
# b = 10
# After:
# a = 10
# b = 5
a = int(input())
b = int(input())

print(f'Before:\na = {a}\nb = {b}')
a, b = b, a
print(f'After:\na = {a}\nb = {b}')
