import calendar


class DVD:

    def __init__(self, name, id_dvd, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id_dvd
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_dvd, name, data, age_restriction):
        day, creation_month, creation_year = data.split('.')
        creation_month, creation_year = int(creation_month), int(creation_year)
        creation_month = calendar.month_name[creation_month]
        return cls(name, id_dvd, creation_year, creation_month, age_restriction)

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month}\
 {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"
