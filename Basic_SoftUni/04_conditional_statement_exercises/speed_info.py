speed = float(input())
var = 0
if speed <= 10:
    var = 'slow'
elif 10 < speed <= 50:
    var = 'average'
elif 50 < speed <= 150:
    var = 'fast'
elif 150 < speed <= 1000:
    var = 'ultra fast'
elif 1000 < speed:
    var = 'extremely fast'
print(var)
