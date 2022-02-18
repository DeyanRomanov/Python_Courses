def age_assignment(*args, **kwargs):
    new_dict = {}
    for names in args:
        for key, value in kwargs.items():
            if key == names[0]:
                new_dict[names] = value
    return new_dict

