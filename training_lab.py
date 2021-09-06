h = float(input()) * 100
w = float(input()) * 100
w -= 100
ranks = w // 70
columns = h // 120
s = ranks * columns - 3
print(s)
