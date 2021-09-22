age = int(input())
# Rules:
# Kid is defined as someone under the age of 14.
# Teen is defined as someone under the age of 18.
# Young adult is defined as someone under the age of 21.
# Adult is defined as someone above the age of 21.
# Note: All the values are inclusive except the last one!
if age <= 14:
    print('drink toddy')
elif age <= 18:
    print('drink coke')
elif age <= 21:
    print('drink beer')
else:
    print('drink whisky')
