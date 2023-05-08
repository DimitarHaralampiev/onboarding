class User:

    def __init__(self, first_name, last_name, age, gender):
        """Initialize variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Return information for user"""
        return f'Fullname: {self.first_name.title() + " " + self.last_name.title()}\n' \
               f'Age: {self.age}\nGender: {self.gender.title()}'

    def great_user(self):
        """Return greetings per user"""
        return f'Greetings {self.first_name.title() + " " + self.last_name.title()}'
