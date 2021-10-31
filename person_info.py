def get_info(**kwargs):
    if kwargs['name'] and kwargs['age'] and kwargs['town']:
        return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
