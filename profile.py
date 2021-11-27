class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
            return

        raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not self.is_logner(value) or not self.is_digits(value) or not self.is_upper(value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value
        return

    def is_logner(self, password):
        return len(password) > 7

    def is_upper(self, password):
        a = [char for char in password if char.isupper()]
        return True if a else False

    def is_digits(self, password):
        a = [char for char in password if char.isdigit()]
        return True if a else False

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
