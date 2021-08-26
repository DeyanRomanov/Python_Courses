a = int(input())
b = int(input())
h = int(input())
percent = float(input())
v = a * b * h
liters = v * 0.001
liters -= (liters * percent / 100)
print(liters)
