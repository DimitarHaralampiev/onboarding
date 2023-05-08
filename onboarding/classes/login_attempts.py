class User:

    INCREMENT_LOGIN_ATTEMPTS = 1
    RESET_LOGIN_ATTEMPTS = 0

    def __init__(self, first_name, last_name, age, gender):
        """Initialize variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Return information for user"""
        return f'Fullname: {self.first_name.title() + " " + self.last_name.title()}\n' \
               f'Age: {self.age}\nGender: {self.gender.title()}\nLogin attempts: {self.login_attempts}'

    def great_user(self):
        """Return greetings per user"""
        return f'Greetings {self.first_name.title() + " " + self.last_name.title()}'

    def increment_login_attempts(self):
        """Increment login attempts"""
        self.login_attempts += self.INCREMENT_LOGIN_ATTEMPTS

    def reset_login_attempts(self):
        """Reset value on login attempts"""
        self.login_attempts = self.RESET_LOGIN_ATTEMPTS


user_one = User('pesho', 'peshov', '15', 'male')
user_one.increment_login_attempts()
print(user_one.describe_user())
print(user_one.great_user())

user_two = User('ivan', 'ivanov', '24', 'male')
user_two.increment_login_attempts()
user_two.increment_login_attempts()
user_two.reset_login_attempts()
print(user_two.describe_user())
print(user_two.great_user())