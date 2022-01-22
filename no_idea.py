n, m = input().split()
numbers = input().split()
a_set = set(input().split())
b_set = set(input().split())
hapiness = 0
for i in numbers:
    if i in a_set:
        hapiness += 1
    elif i in b_set:
        hapiness -= 1

print(hapiness)
